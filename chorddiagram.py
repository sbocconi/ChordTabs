import os
from pathlib import Path

from instrument import Instrument

TOP_MARGIN = 20
BOTTOM_MARGIN = 6


BASE_TAB_WIDTH = 15.0
TAB_SPACING = 1.0
LEFT_MARGIN = 20
RIGHT_MARGIN = 20
TAB_SCALE = 1.4

ROW_SPACING = 2.0 # Vertical spacing between rows in PDF (in mm)
CHAPTER_SPACING = 5.0 # Vertical spacing between rows in PDF (in mm)


class ChordDiagram:
    TMP_FILE = '/tmp/tmp.ly'
    LILYPOND_BIN = '/opt/homebrew/bin/lilypond'
    ROOT = "./GeneratedTabs"

    

    def __init__(self):
        pass        
        # breakpoint()

    @classmethod
    def chord_to_lilypond(cls, tab, nr_strings):
        """
        tab: list of (note, string, fret)
        string = 6 (low E) … 1 (high E)
        """
        diagram = [f"(mute {i})" for i in reversed(range(1, nr_strings+1))]
        # breakpoint()
        for note, string, fret in tab.tab_as_tuple_array():
            # breakpoint()
            diagram[nr_strings - string] = f'(place-fret {string} {fret} "{note}")'

        return "\\fret-diagram-verbose #'(" + " ".join(diagram) + ')'

    @classmethod
    def make_tab(cls, code):

        return f"\n      \scale #'({TAB_SCALE} . {TAB_SCALE}) {{" + code + "}"

    @classmethod
    def make_line(cls, line_items:list[str], end:bool=False)->list[str]:
        row_items = []
        
        row_items.append("    \\fill-line { " + " ".join(line_items) + "\n    }")
        row_items.append(f"    \\vspace #{ROW_SPACING}")
        if end:
            row_items.append("  }")
        return row_items
    

    @classmethod
    def make_header(cls, title:str, composer:str, description:str, chapters:list) -> list:
        book = []
        header = r"""
\version "2.24.4"
\book {

\paper {
    % https://lilypond.org/doc/v2.25/Documentation/notation/the-paper-block
  #(set-paper-size "a4" 'portrait)
  
  top-margin = """ + f"{TOP_MARGIN}" + r"""\mm
  bottom-margin = """ + f"{BOTTOM_MARGIN}" + r"""\mm
  %left-margin = """ + f"{LEFT_MARGIN}" + r"""\mm % The margin between the left edge of the page and the start of the staff lines in unindented systems. If the paper size is modified, this dimension’s default value is scaled accordingly. If left-margin is unset, and both line-width and right-margin are set, then left-margin is set to (paper-width - line-width - right-margin). If only line-width is set, then both margins are set to ((paper-width - line-width) / 2), and the systems are consequently centered on the page.
  %right-margin = """ + f"{RIGHT_MARGIN}" + r"""\mm % The margin between the right edge of the page and the end of the staff lines in non-ragged systems. If the paper size is modified, this dimension’s default value is scaled accordingly. If right-margin is unset, and both line-width and left-margin are set, then right-margin is set to (paper-width - line-width - left-margin). If only line-width is set, then both margins are set to ((paper-width - line-width) / 2), and the systems are consequently centered on the page.
  %line-width = 170\mm leave unset to have line-width = (paper-width - left-margin - right-margin)
  
  check-consistency = ##t %If this is true (the default value), print a warning if left-margin, line-width, and right-margin do not exactly add up to paper-width, and replace each of these (except paper-width) with their default values (scaled to the paper size if necessary). If set to false, ignore any inconsistencies and allow systems to run off the edge of the page. 
  
  two-sided = ##f % If set to true, use inner-margin, outer-margin and binding-offset to determine margins depending on whether the page number is odd or even. This overrides left-margin and right-margin.
  ragged-bottom = ##t %If this is set to #t, systems will be set at their natural spacing, neither compressed nor stretched vertically to fit the page. 
  ragged-right = ##t %If set to #t, systems will not fill the line width. Instead, systems end at their natural horizontal length. Default: #t for scores with only one system, and #f for scores with two or more systems.
  tocItemMarkup = \tocItemWithDotsMarkup
}

\header {
  title = """ + f'"{title}"' + r"""
  composer = """ + f'"{composer}"' + r"""
}
\markup {
  \vspace #3
  \fontsize #1 \italic \fontCaps {
    \wordwrap-string """ + f'"{description}"' + r"""
  }
  \vspace #3
}
\pageBreak
\markuplist \table-of-contents
\pageBreak

"""
        book.append(header)
        book.extend(chapters)
        book.append("}")
        return book
    
    @classmethod
    def make_chapter(cls, nr_strings:int, fret_count:int, chapter_title:str, rows:list, chapter_subtitle:str=None, chapter_desc:str=None)->list:

        chapter_rows = []
        if chapter_subtitle != None:
            subtitle = r"""
  \vspace #1
  \fontsize #1 \italic {
    \wordwrap-string """ + f'"{chapter_subtitle}"' + r"""
  }
"""
        else:
            subtitle = ""

        if chapter_desc != None:
            desc = r"""
  \vspace #1
  \fontsize #1 """ + f'"{chapter_desc}"'
        else:
            desc = ""

        chapter = r"""
\tocItem \markup """ + f'"{chapter_title}"' + r"""
\markuplist {
  \override #'(fret-diagram-details . (
    (finger-code . in-dot)
    (dot-color . black)
    (dot-label-color . white)
    (dot-radius . 0.55)
    (dot-label-font-mag . 0.8)
    (string-count . """ + f'{nr_strings}' + r""")
    (fret-count . """ + f'{fret_count}' + r""")
  ))

  {
    \fontsize #3 \bold """ + f'"{chapter_title}"' + subtitle + desc + r"""
    \vspace #""" + f'{ROW_SPACING}' + r"""
"""
        chapter_rows.append(chapter)
        chapter_rows.extend(rows)
        chapter_rows.append("}")
        return chapter_rows
    
    @classmethod
    def make_chapters(cls, tabs:object, nr_strings:int, fret_count:int)->list:
        """
        Creates the chapters by filling their rows for every chapter
        """
        nr_col = cls.nr_tabs_line()
        all_chapters = []
        for key in tabs:
            rows = []
            line_items = []
            for index, tab in enumerate(tabs[key]["Tabs"]):
                if not tabs[key]["Selected"][index]:
                    continue
                # check we already have enough diagrams and horizontal spaces
                if len(line_items) >= (2*nr_col-1):
                    rows.extend(cls.make_line(line_items))
                    # breakpoint()
                    line_items = []
                # if len(rows) > 20:
                #     break
                line_items.append(cls.make_tab(cls.chord_to_lilypond(tab,nr_strings)))
                if len(line_items) < (2*nr_col-1):
                    line_items.append(f'\\hspace #{TAB_SPACING}')            
            if len(line_items) > 0:
                rows.extend(cls.make_line(line_items, end=True))
        # Combine header items (if any) with grid rows
        # breakpoint()
            all_chapters.extend(cls.make_chapter(nr_strings, fret_count, tabs[key]["Desc"], rows))
        return all_chapters

    @classmethod
    def nr_tabs_line(cls):
        """
        For A4 paper (21cm wide) calculate appropriate number of tabs per row based on diagram size and spacing.
        Each chord diagram is BASE_TAB_WIDTH wide at size 1.0.
        Returns number of columns
        """
        # Calculate diagram total width
        diagram_width = BASE_TAB_WIDTH * TAB_SCALE
        # A4 paper is 21cm wide
        a4_width = 210.0
        available_space = a4_width - LEFT_MARGIN - RIGHT_MARGIN
        nr_tabs = (available_space + TAB_SPACING) // (diagram_width + TAB_SPACING)
        # breakpoint()
        return nr_tabs
    
    @classmethod
    def create_lp(cls, title, composer, description, tabs, nr_strings, fret_count):
        # breakpoint()
        ly_grid =  cls.make_header(title, composer, description, cls.make_chapters(tabs, nr_strings, fret_count))

        with open(cls.TMP_FILE, "w") as f:
            f.write("\n".join(ly_grid))
        
    @classmethod
    def create_pdf(cls, out_bin):
        # out_path = self.get_fullpath(out_bin)
        out_path = out_bin
        # call the pdf creator on the lilypond path
        os.system('%(lilypond)s %(params)s -o %(output)s %(input)s' % {
            'lilypond': cls.LILYPOND_BIN,
            'params': '--pdf',
            'output': out_path,
            'input': cls.TMP_FILE,
        })
        return True
    
    @classmethod
    def create_png(cls, out_bin):
        out_path = cls.get_fullpath(out_bin)
        # call the png creator on the lilypond path
        os.system('%(lilypond)s %(params)s -o %(output)s %(input)s' % {
            'lilypond': cls.LILYPOND_BIN,
            'params': '--png -dresolution=1200 -dbackend=eps',
            'output': out_path,
            'input': cls.TMP_FILE,
        })
        # clean up excess files
        # LILYPOND_GARBAGE = ['-systems.count', '-1.eps', '-systems.tex', '-systems.texi', '.eps']
        # files = ' '.join([path + garbage for garbage in LILYPOND_GARBAGE])
        # os.system('rm ' + files)
        # return true on success
        return True


    @classmethod
    def get_fullpath(cls, out_bin):
        # breakpoint()
        out_path = Path(cls.ROOT, cls.chord_signature(),out_bin, f"{cls.chord_signature()}_{cls.chord_type}")
        if not out_path.parent.exists():
            out_path.parent.mkdir(parents=True)
        return out_path

    @classmethod
    def chord_signature(cls):
        prfx = '.'.join(cls.chord_notes)
        return prfx
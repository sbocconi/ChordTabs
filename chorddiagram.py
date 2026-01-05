import os
from pathlib import Path

from instrument import Instrument

BASE_DIAGRAM_WIDTH = 2.0
ROW_SPACING = 5.0 # Vertical spacing between rows in PDF (in mm)
COLUMN_SPACING = 2.0

class ChordDiagram:
    TMP_FILE = '/tmp/tmp.ly'
    LILYPOND_BIN = '/opt/homebrew/bin/lilypond'
    ROOT = "./GeneratedTabs"

    

    def __init__(self, top_margin:int=5, bottom_margin:int=6, left_margin:int=10, right_margin:int=10, diagram_scale:float=1.4):
        self.top_margin = top_margin
        self.bottom_margin = bottom_margin
        self.left_margin = left_margin
        self.right_margin = right_margin
        self.diagram_scale = diagram_scale
        # breakpoint()

    def make_header(self, title, composer, description) -> str:
        header = r"""
\version "2.24.4"
\book {

\paper {
    % https://lilypond.org/doc/v2.25/Documentation/notation/the-paper-block
  #(set-paper-size "a4" 'portrait)
  
  top-margin = """ + f"{self.top_margin}" + r"""\mm
  bottom-margin = """ + f"{self.bottom_margin}" + r"""\mm
  %left-margin = """ + f"{self.left_margin}" + r"""\mm % The margin between the left edge of the page and the start of the staff lines in unindented systems. If the paper size is modified, this dimension’s default value is scaled accordingly. If left-margin is unset, and both line-width and right-margin are set, then left-margin is set to (paper-width - line-width - right-margin). If only line-width is set, then both margins are set to ((paper-width - line-width) / 2), and the systems are consequently centered on the page.
  %right-margin = """ + f"{self.right_margin}" + r"""\mm % The margin between the right edge of the page and the end of the staff lines in non-ragged systems. If the paper size is modified, this dimension’s default value is scaled accordingly. If right-margin is unset, and both line-width and left-margin are set, then right-margin is set to (paper-width - line-width - left-margin). If only line-width is set, then both margins are set to ((paper-width - line-width) / 2), and the systems are consequently centered on the page.
  %line-width = 170\mm leave unset to have line-width = (paper-width - left-margin - right-margin)
  
  check-consistency = ##t %If this is true (the default value), print a warning if left-margin, line-width, and right-margin do not exactly add up to paper-width, and replace each of these (except paper-width) with their default values (scaled to the paper size if necessary). If set to false, ignore any inconsistencies and allow systems to run off the edge of the page. 
  
  two-sided = ##f % If set to true, use inner-margin, outer-margin and binding-offset to determine margins depending on whether the page number is odd or even. This overrides left-margin and right-margin.
  
  tocItemMarkup = \tocItemWithDotsMarkup
}

\header {
  title = """ + f'"{title}"' + r"""
  composer = """ + f'"{composer}"' + r"""
}
%\fontsize #1 \italic {
%    \wordwrap-string """ + f'"description"' + r"""
%}

\markuplist \table-of-contents
\pageBreak

"""
        return header
    
    @classmethod
    def make_chapter(cls, string_count:int, fret_count:int, chapter_title:str, chapter_subtitle:str, chapter_desc:str):

        chapter = r"""
\tocItem \markup """ + f'"{chapter_title}"' + r"""
\markuplist {
\override #'(fret-diagram-details . (
    (finger-code . in-dot)
    (dot-color . black)
    (dot-label-color . white)
    (dot-radius . 0.55)
    (dot-label-font-mag . 0.8)
    (string-count . """ + f'{string_count}' + r""")
    (fret-count . """ + f'{fret_count}' + r""")
  ))

  {
  \fontsize #4 \bold """ + f'"{chapter_title}"' + r"""
  \vspace #1
  \fontsize #1 \italic {
    \wordwrap-string """ + f'"{chapter_subtitle}"' + r"""
  }
  \vspace #1
  \fontsize #3 \bold """ + f'"{chapter_desc}"' + r"""
  \vspace #3
"""
        return chapter
    

    def calculate_nr_cols(self):
        """
        For A4 paper (21cm wide) calculate appropriate number of tabs per row based on diagram size and spacing.
        Each chord diagram is BASE_DIAGRAM_WIDTH wide at size 1.0.
        Returns number of columns
        """
        # Calculate diagram total width
        diagram_width = BASE_DIAGRAM_WIDTH * self.diagram_scale
        # A4 paper is 21cm wide
        a4_width = 210.0
        available_space = a4_width - self.left_margin - self.right_margin
        nr_col = (available_space + COLUMN_SPACING) // (diagram_width + COLUMN_SPACING)
        
        return nr_col
    
    def create_lp(self, title, composer, description, tabs, string_count, fret_count):
        # breakpoint()
        ly_grid =  self.make_header(title, composer, description) + self.make_grid(tabs, string_count, fret_count) + '}'

        with open(self.TMP_FILE, "w") as f:
            f.write(ly_grid)
        
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

    
    def make_grid(self, tabs, string_count, fret_count):
        """
        Creates a grid layout with configurable spacing between rows
        """
        nr_col = self.calculate_nr_cols()
        rows = []
        for key in tabs:
            line_items = []
            for index, tab in enumerate(tabs[key]["Tabs"]):
                if not tabs[key]["Selected"][index]:
                    continue
                # check we already have enough diagrams and horizontal spaces
                if len(line_items) >= (2*nr_col-1):
                    rows.append("\\fill-line { " + " ".join(line_items) + " }")
                    rows.append(f"\\vspace #{ROW_SPACING}")
                    line_items = []
                # if len(rows) > 20:
                #     break
                code = self.chord_to_lilypond(tab,string_count)
                line_items.append(code)
                if len(line_items) < (2*nr_col-1):
                    line_items.append(f'\\hspace #{COLUMN_SPACING}')            
            if len(line_items) > 0:
                rows.append("\\fill-line { \\scale #\'" +  f'({self.diagram_scale} . {self.diagram_scale})' +"{"  + " ".join(line_items) + " } }")
                rows.append(f"\\vspace #{ROW_SPACING}")
        # Combine header items (if any) with grid rows
        # breakpoint()
        all_items = self.make_chapter(string_count, fret_count, tabs[key]["Desc"], "chapter_subtitle", "chapter_desc") + "\n  ".join(rows)
        return all_items + "\n}\n}"


    def create_pdf(self, out_bin):
        # out_path = self.get_fullpath(out_bin)
        out_path = out_bin
        # call the pdf creator on the lilypond path
        os.system('%(lilypond)s %(params)s -o %(output)s %(input)s' % {
            'lilypond': self.LILYPOND_BIN,
            'params': '--pdf',
            'output': out_path,
            'input': self.TMP_FILE,
        })
        return True
    
    def create_png(self, out_bin):
        out_path = self.get_fullpath(out_bin)
        # call the png creator on the lilypond path
        os.system('%(lilypond)s %(params)s -o %(output)s %(input)s' % {
            'lilypond': self.LILYPOND_BIN,
            'params': '--png -dresolution=1200 -dbackend=eps',
            'output': out_path,
            'input': self.TMP_FILE,
        })
        # clean up excess files
        # LILYPOND_GARBAGE = ['-systems.count', '-1.eps', '-systems.tex', '-systems.texi', '.eps']
        # files = ' '.join([path + garbage for garbage in LILYPOND_GARBAGE])
        # os.system('rm ' + files)
        # return true on success
        return True


    def get_fullpath(self, out_bin):
        # breakpoint()
        out_path = Path(self.ROOT, self.chord_signature(),out_bin, f"{self.chord_signature()}_{self.chord_type}")
        if not out_path.parent.exists():
            out_path.parent.mkdir(parents=True)
        return out_path

    def chord_signature(self):
        prfx = '.'.join(self.chord_notes)
        return prfx
import os
from pathlib import Path

from instrument import Instrument

pdf_tabs_per_row = 8 # Number of chord diagrams per row in PDF
pdf_diagram_size = 1.5 # Size scaling factor for chord diagrams (1.5 = default larger size, 1.0 = normal)
pdf_row_spacing = 5.0 # Vertical spacing between rows in PDF (in mm)
pdf_column_spacing = 2.0

class ChordDiagram:
    TMP_FILE = '/tmp/tmp.ly'
    LILYPOND_BIN = '/opt/homebrew/bin/lilypond'
    ROOT = "./GeneratedTabs"
    

    def __init__(self, chord_notes:list, chord_type:str, tabs:list, instrument:Instrument, title:str=None, description:str=None):
        self.chord_notes = chord_notes
        self.chord_type = chord_type
        self.tabs = tabs
        self.instrument = instrument
        self.title = title
        self.description = description
        # breakpoint()

    
    def calculate_line_width_and_margins(self):
        """
        Calculate appropriate line-width based on number of columns, diagram size, and spacing.
        For A4 paper (21cm wide), we adjust margins to fit the content.
        Each chord diagram is approximately 2cm wide at size 1.0.
        Returns (line_width_cm, left_margin_mm, right_margin_mm)
        """
        # Base width per diagram (in cm) at size 1.0 (default is now 1.5)
        base_diagram_width = 2.0
        # Calculate total width needed
        diagram_width = base_diagram_width * pdf_diagram_size
        total_spacing = (pdf_tabs_per_row - 1) * (pdf_column_spacing / 10.0)  # Convert mm to cm
        needed_width = pdf_tabs_per_row * diagram_width + total_spacing
        
        # Add some padding (10%)
        calculated_width = needed_width * 1.1
        
        # A4 paper is 21cm wide
        a4_width = 21.0
        # Minimum margins we want to keep
        min_margin = 5.0  # 5mm minimum margin
        max_line_width = a4_width - (2 * min_margin / 10.0)  # Convert mm to cm
        
        if calculated_width <= max_line_width:
            # Use calculated width, standard margins
            line_width = calculated_width
            left_margin = 15.0
            right_margin = 15.0
        else:
            # Use maximum width, smaller margins
            line_width = max_line_width
            remaining_space = a4_width - line_width
            margin = remaining_space / 2 * 10.0  # Convert cm to mm
            left_margin = margin
            right_margin = margin
        
        return (line_width, left_margin, right_margin)
    
    def create_lp(self):
        line_width_cm, left_margin_mm, right_margin_mm = self.calculate_line_width_and_margins()
        ly_grid = r"""
        \version "2.24.2"
        \paper {
            top-margin = 10\mm
            bottom-margin = 10\mm
            left-margin = """ + f"{left_margin_mm:.1f}\\mm" + r"""
            right-margin = """ + f"{right_margin_mm:.1f}\\mm" + r"""
            line-width = """ + f"{line_width_cm:.1f}\\cm" + r"""
            page-breaking = #ly:optimal-breaking
        }

        \markup {
        \override #'(fret-diagram-details . (
            (finger-code . in-dot)        ; put labels inside the dots
            (dot-color . black)           ; black filled dots
            (dot-label-color . white)     ; white note names
            (dot-radius . 0.55)           ; size of dots
            (dot-label-font-mag . 0.8)    ; label font size
            (fret-count . 5)              ; number of frets shown
        ))
        """ + self.make_grid() + '}'

        with open(self.TMP_FILE, "w") as f:
            f.write(ly_grid)
        
    def chord_to_lilypond(self,tab):
        """
        tab: list of (note, string, fret)
        string = 6 (low E) … 1 (high E)
        """
        diagram = [f"(mute {i})" for i in reversed(range(1, self.instrument.nr_strings+1))]
        # breakpoint()
        for note, string, fret in tab:
            # breakpoint()
            diagram[self.instrument.nr_strings - string] = f'(place-fret {string} {fret} "{note}")'

        return "\\fret-diagram-verbose #'(" + " ".join(diagram) + ')'

    def make_header_items(self):
        """
        Creates header items (title and description) if provided
        Returns list of header markup items
        """
        header_items = []
        if self.title:
            # Escape special characters in title for LilyPond
            title_escaped = self.title.replace('\\', '\\textbackslash{}').replace('"', '\\"')
            header_items.append(f'\\vspace #4')
            header_items.append(f'\\fontsize #4 \\bold "{title_escaped}"')
        if self.description:
            # Escape special characters in description
            desc_escaped = self.description.replace('\\', '\\textbackslash{}').replace('"', '\\"')
            header_items.append(f'\\vspace #2')
            header_items.append(f'\\wordwrap-string "{desc_escaped}"')
        if header_items:
            header_items.append(f'\\vspace #4')
        return header_items
    
    def make_grid(self):
        """
        Creates a grid layout with configurable spacing between rows
        """
        rows = []
        num_rows = (len(self.tabs) + pdf_tabs_per_row - 1) // pdf_tabs_per_row  # Ceiling division
        for row_idx, i in enumerate(range(0, len(self.tabs), pdf_tabs_per_row)):
            line_items = []
            row_tabs = self.tabs[i:min(i+pdf_tabs_per_row,len(self.tabs))]
            for tab_idx, tab in enumerate(row_tabs):
                # breakpoint()
                code = self.chord_to_lilypond(tab)
                # Apply size scaling to each diagram (always apply scale for consistency)
                diagram_code = f'\\scale #({pdf_diagram_size} . {pdf_diagram_size}) {{ \\column {{ {code} }}}}'
                line_items.append(diagram_code)
                # Add horizontal spacing after each diagram except the last
                # Convert mm to staff-space units (approximately 1 staff-space = 0.75mm)
                if tab_idx < len(row_tabs) - 1:
                    hspace_staff = round(pdf_column_spacing / 0.75) if pdf_column_spacing > 0 else 1
                    line_items.append(f'\\hspace #{hspace_staff}')
            rows.append("\\line { " + " ".join(line_items) + " }")
            # Add configurable spacing between rows (skip spacing after last row)
            # Convert mm to staff-space units (approximately 1 staff-space = 0.75mm)
            if row_idx < num_rows - 1:
                vspace_staff = round(pdf_row_spacing / 0.75) if pdf_row_spacing > 0 else 1
                rows.append(f"\\vspace #{vspace_staff}")
        # Combine header items (if any) with grid rows
        all_items = self.make_header_items() + rows
        return "\\column {\n  " + "\n  ".join(all_items) + "\n}"


    def create_pdf(self, out_bin):
        out_path = self.get_fullpath(out_bin)
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
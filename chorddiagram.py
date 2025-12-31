import os
from pathlib import Path

from instrument import Instrument

class ChordDiagram:
    TMP_FILE = '/tmp/tmp.ly'
    LILYPOND_BIN = '/opt/homebrew/bin/lilypond'
    ROOT = "./GeneratedTabs"
    

    def __init__(self, chord_notes:list, chord_type:str, tabs:list, instrument:Instrument, ncols:int=8):
        self.chord_notes = chord_notes
        self.chord_type = chord_type
        self.tabs = tabs
        self.instrument = instrument
        self.ncols = ncols
        # breakpoint()

    
    def create_lp(self):
        ly_grid = r"""
        \version "2.24.2"
        \paper {
            top-margin = 10\mm
            line-width = 15.5\cm
        }

        \markup {
        \override #'(fret-diagram-details . (
            (finger-code . in-dot)        ; put labels inside the dots
            (dot-color . black)           ; black filled dots
            (dot-label-color . white)     ; white note names
            (dot-radius . 0.55)           ; size of dots
            (dot-label-font-mag . 0.8)    ; label font size
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

    def make_grid(self):
        """
        """
        rows = []
        for i in range(0, len(self.tabs), self.ncols):
            line_tabs = []
            for tab in self.tabs[i:min(i+self.ncols,len(self.tabs))]:
                # breakpoint()
                code = self.chord_to_lilypond(tab)
                line_tabs.append(f'\\column {{ {code} }}')
            rows.append("\\line { " + " ".join(line_tabs) + " }")
            rows.append("\\line { }")
        return "\\column {\n  " + "\n  ".join(rows) + "\n}"


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
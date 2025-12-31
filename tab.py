from chorddiagram import ChordDiagram
from instrument import Instrument

class Tab:
    inputs = {
        'max_dist':{
            'desc': "The max distance between fretted notes",
            'type' : int,
            'default' : 5
        },
        'min_fret_pos':{
            'desc': "Fret of the lowest fretted note",
            'type' : int,
            'default' : -1
        },
        'max_fret_pos':{
            'desc': "Fret of the highest fretted note",
            'type' : int,
            'default' : -1
        },
        'allow_open_strings':{
            'desc': "Allow open strings in the chord",
            'type' : bool,
            'default' : False
        },
        'bottom_top_notes':{
            'desc': "Specify the bottom and top note",
            'type' : tuple,
            'subtype' : str,
            'default' : None,
            'wildcard' : '*'
        },
        'prefer_strings': {
            'desc': "What strings should be part of the voicing",
            'type' : tuple,
            'subtype' : int,
            'default' : None
        },
        'avoid_strings': {
            'desc': "What strings should NOT be part of the voicing",
            'type' : tuple,
            'subtype' : int,
            'default' : None
        },
        'gap_top_strings': {
            'desc': "Allow string gaps in the highest part of the chord",
            'type' : bool,
            'default' : True
        },
        # 'partial': {
        #     'type' : bool,
        #     'default' : False
        # }
    }
    def __init__(self, inversion, fret_nrs, chosen_strings, open_string_notes):
        # breakpoint()
        # We prefer to have tabs from lower string to highest string
        self.inversion = tuple(reversed(inversion))
        self.fret_nrs = tuple(reversed(fret_nrs))
        self.chosen_strings = tuple(reversed(chosen_strings))
        self.open_string_notes = tuple(reversed(open_string_notes))
    
        # breakpoint()

    def has_open_strings(self):
        return True if 0 in self.fret_nrs else False

    def gap_top_strings(self, allow_open_strings:bool):
        # Returns False if there is no gap in the strings among n-1 higher strings
        # or the gap strings are notes in the chord if open strings are allowed
        
        for i in reversed(range(2,len(self.chosen_strings))):
            # Are strings consecutive (diff is 1)?
            if self.chosen_strings[i] != (self.chosen_strings[i-1]-1):
                if allow_open_strings == False:
                    # breakpoint()
                    return True
                # The gap strings can be played (a vuoto) if their notes belong to the chord
                # ids of strings in the gap
                for j in range(self.chosen_strings[i]+1,self.chosen_strings[i-1]):
                    # "any" is due to the fact that notes have enharmonics, it is enough that one is contained in the inversion
                    if not any(jj in self.inversion for jj in self.open_string_notes[len(self.open_string_notes)-j]):
                        return True
        return False

    def nr_gaps_strings(self):
        # Returns the nr of non adjacent strings in a tab
        nr_gap = 0
        for i in reversed(range(1,len(self.chosen_strings))):
            gap = self.chosen_strings[i] - self.chosen_strings[i-1] - 1
            if gap > 0:
                nr_gap = nr_gap + 1
        return nr_gap

    def max_fret_dist(self):
        # Returns the max nr of frets between any two positions
        # not counting open strings
        max_fret_nr = 0
        min_fret_nr = 1000
        for i in range(len(self.fret_nrs)):
            if self.fret_nrs[i] != 0:
                if self.fret_nrs[i] > max_fret_nr:
                    max_fret_nr = self.fret_nrs[i]
                if self.fret_nrs[i] < min_fret_nr:
                    min_fret_nr = self.fret_nrs[i]
        return max_fret_nr - min_fret_nr + 1
    
    def min_fret_pos(self):
        # Returns the lowest fret position
        min_fret_nr = 1000
        for i in range(len(self.fret_nrs)):
            if self.fret_nrs[i] != 0:
                if self.fret_nrs[i] < min_fret_nr:
                    min_fret_nr = self.fret_nrs[i]
        return min_fret_nr
    
    def max_fret_pos(self):
        # Returns the lowest fret position
        max_fret_nr = 0
        for i in range(len(self.fret_nrs)):
            if self.fret_nrs[i] != 0:
                if self.fret_nrs[i] > max_fret_nr:
                    max_fret_nr = self.fret_nrs[i]
        return max_fret_nr

    def is_preferred_inversion(self, bottom_top_notes):
        if bottom_top_notes[0] != Tab.inputs['bottom_top_notes']['wildcard'] and self.inversion[0] != bottom_top_notes[0]:
            return False 
        if bottom_top_notes[-1] != Tab.inputs['bottom_top_notes']['wildcard'] and self.inversion[-1] != bottom_top_notes[-1]:
            return False 

        return True

    def are_preferred_strings(self, preferred):
        # breakpoint()
        for idx in range(len(preferred)):
            if not preferred[idx] in self.chosen_strings:
                    return False
        return True
    
    def are_avoided_strings(self, avoid_strings):
        # breakpoint()
        for idx in range(len(avoid_strings)):
            if avoid_strings[idx] in self.chosen_strings:
                    return True
        return False

    def get_label(self):
        return ', '.join(self.inversion)

    def get_tab(self):
        # returns an array of the form [('G', 6, 3), ('Bb', 5, 1), ('E', 4, 2), ('C', 3, 5)]
        return [i for i in zip(self.inversion,self.chosen_strings,self.fret_nrs)]
    
    def print_tab(self):
        # breakpoint()
        print(f"(note,strings,fret): {self.get_tab()}, max dist: {self.max_fret_dist()}")

class Tabs:
    
    def __init__(self, chord, instrument:Instrument):
        self.chord = chord
        self.all_tabs = {}
        self.selected_tabs = {}
        self.instrument = instrument
    
    def add(self, key, tab):
        if key not in self.all_tabs:
            self.all_tabs[key] = []
        self.all_tabs[key].append(tab)
    
    def filter_tabs(self, max_dist:int, allow_open_strings:bool, bottom_top_notes:tuple, prefer_strings:tuple, avoid_strings:tuple, gap_top_strings:bool, 
                   min_fret_pos:int=-1,max_fret_pos:int=-1):
        
        result = False
        chord_bin = f"max_dist={max_dist}_openstr={allow_open_strings}_bottomtop={self.prtable_tpl(bottom_top_notes)}_prefstr={self.prtable_tpl(prefer_strings)}"
        chord_bin = f"{chord_bin}_avoidstr={self.prtable_tpl(avoid_strings)}_gaptop={gap_top_strings}_minfret={min_fret_pos}_maxfret{max_fret_pos}"
        self.chord_bin = chord_bin

        for key in self.all_tabs:
            selected_tabs = self.all_tabs[key].copy()
            
            if max_dist != -1:
                selected_tabs[:] = [tab for tab in selected_tabs if tab.max_fret_dist() <= max_dist]
            
            # breakpoint()

            if allow_open_strings != True:
                selected_tabs[:] = [tab for tab in selected_tabs if not tab.has_open_strings()]

            if bottom_top_notes != None:
                # breakpoint()
                selected_tabs[:] = [tab for tab in selected_tabs if tab.is_preferred_inversion(bottom_top_notes)]

            if prefer_strings != None:
                # breakpoint()
                selected_tabs[:] = [tab for tab in selected_tabs if tab.are_preferred_strings(prefer_strings)]

            if avoid_strings != None:
                # breakpoint()
                selected_tabs[:] = [tab for tab in selected_tabs if not tab.are_avoided_strings(avoid_strings)]
            
            if gap_top_strings == False:
                selected_tabs[:] = [tab for tab in selected_tabs if not tab.gap_top_strings(allow_open_strings)]

            if min_fret_pos != -1:
                selected_tabs[:] = [tab for tab in selected_tabs if tab.min_fret_pos()>=min_fret_pos]
            
            if max_fret_pos != -1:
                selected_tabs[:] = [tab for tab in selected_tabs if tab.max_fret_pos()<=max_fret_pos]
            
            # breakpoint()
            if len(selected_tabs) == 0:
                print(f"No tab satisfies selection for key {key}")
                self.selected_tabs[key] = []
            else:
                self.selected_tabs[key] = selected_tabs
                result = True
        
        return result

    def print_tabs(self, all:bool=False):
        if all:
            out_tabs = self.all_tabs
        else:
            out_tabs = self.selected_tabs
        
        for key in out_tabs:
            tabs_to_print = []
            for tab in out_tabs[key]:
                tab.print_tab()
                tabs_to_print.append(tab.get_tab())
        
            if len(tabs_to_print) > 0:
                # breakpoint()
                diagram = ChordDiagram(self.chord, key, tabs_to_print, self.instrument)
                diagram.create_lp()
                diagram.create_pdf(self.chord_bin)

    @classmethod
    def prtable_tpl(cls, tpl:tuple)->str:
        if tpl == None:
            return "No"
        # breakpoint()
        ret = ','.join(map(str,tpl))
        return ret
        

    
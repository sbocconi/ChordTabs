import itertools

from chorddiagram import ChordDiagram
from instrument import Instrument
from globals import SEL_DEGREES, DEGREES


class Tab:
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

    def tab_as_tuple_array(self):
        # returns an array of the form [('G', 6, 3), ('Bb', 5, 1), ('E', 4, 2), ('C', 3, 5)]
        return [i for i in zip(self.inversion,self.chosen_strings,self.fret_nrs)]
    
    def print_tab(self):
        # breakpoint()
        print(f"(note,strings,fret): {self.tab_as_tuple_array()}, max dist: {self.max_fret_dist()}")

class Tabs:
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
    }

    
    def __init__(self, chord:list, instrument:Instrument, min_nr_notes:int):
        # Chord is an array with degrees 1,3,5,7,9,11,13 possibly missing
        self.chord = chord
        self.instrument = instrument
        self.min_nr_notes = min_nr_notes
        self.all_tabs = {}
        self.selected_tabs = {}
        self.pdf_title = f"Tabs for the chord: {self.chord}"
        self.pdf_description = "Generated automatically by Farback"


        self.complete_combinations()
    
    def add(self, key, note_seq,fret_nrs,chosen_strings, instrument):
        if key not in self.all_tabs:
            self.all_tabs[key] = []
        tab = Tab(note_seq,fret_nrs,chosen_strings, instrument.open_string_notes())
        self.all_tabs[key].append(tab)
    
    def create_tabs(self, key, chosen_notes):
    # Permutations of the notes in the chord
    # Creates all possible positions for the given notes (order is meaningful)
        for note_seq in itertools.permutations(chosen_notes):
            # Here we pick all distinct groups of strings size=length(note_seq) (order not important)
            for chosen_strings in itertools.combinations(self.instrument.strings_idx, len(note_seq)):
                # Permutations in the strings to fret
                all_fret_nrs = [ [ ] for i in range(len(note_seq))]
                for i in range(len(note_seq)):
                    # Calculate all positions of a particular note on i-th string
                    all_fret_nrs[i] = [ idx for idx in range(self.instrument.notes_per_string()) if note_seq[i] in self.instrument.note_at(chosen_strings[i],idx)]
                    # breakpoint()
                for fret_nrs in itertools.product(*all_fret_nrs):
                    # Add a tab for each combination of positions
                    self.add(key, note_seq,fret_nrs,chosen_strings, self.instrument)


    def complete_combinations(self)-> None:
        # We had all combinations that do not have necessarily a logic
        # This group is made not to overlap with logic combinations
        new_degrees = {}
        for nr_notes_in_chord in range(self.min_nr_notes,len(self.chord)+1):
            # breakpoint()
            # Here we pick all distinct groups of length nr_notes_in_chord (order not important)
            for chosen_degrees in itertools.combinations(DEGREES.keys(), nr_notes_in_chord):
                sel_degrees_present = False
                # print(f"chosen_degrees: {chosen_degrees}")
                for key in SEL_DEGREES.keys():
                    if SEL_DEGREES[key]["Degrees"] == list(chosen_degrees):
                        sel_degrees_present = True
                        # breakpoint()
                        break
                if not sel_degrees_present:
                    key = f"{chosen_degrees}_degrees"
                    new_degrees[key] = {}
                    new_degrees[key]["Desc"] = f"All combinations of {[DEGREES[i] for i in chosen_degrees]}"
                    new_degrees[key]["Degrees"] = list(chosen_degrees)
        self.complete_degrees = SEL_DEGREES | new_degrees
        # breakpoint()

    def generate_tabs(self)-> None:
        for key in self.complete_degrees.keys():
            degrees_present = True
            for degree in self.complete_degrees[key]["Degrees"]:
                if self.chord[degree] == '':
                    degrees_present = False
                    break
            if degrees_present:
                self.create_tabs(key, [self.chord[i] for i in self.complete_degrees[key]["Degrees"]])    

        


    def filter_tabs(self, max_dist:int, allow_open_strings:bool, bottom_top_notes:tuple, prefer_strings:tuple, avoid_strings:tuple, gap_top_strings:bool, 
                   min_fret_pos:int=-1,max_fret_pos:int=-1):
        
        result = False
        # Store PDF layout parameters
        
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
            print(f'{self.complete_degrees[key]["Desc"]}')
            for tab in out_tabs[key]:
                # tab.print_tab()
                tabs_to_print.append(tab.tab_as_tuple_array())
        
            # if len(tabs_to_print) > 0:
            #     # breakpoint()
            #     diagram = ChordDiagram(self.chord, key, tabs_to_print, self.instrument, 
            #                           title=self.pdf_title,
            #                           description=self.pdf_description)
            #     diagram.create_lp()
            #     diagram.create_pdf(self.chord_bin)

    @classmethod
    def prtable_tpl(cls, tpl:tuple)->str:
        if tpl == None:
            return "No"
        # breakpoint()
        ret = ','.join(map(str,tpl))
        return ret
        

    
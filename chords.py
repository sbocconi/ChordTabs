import itertools

from instrument import Instrument
from tab import Tab, Tabs


class ExitFromUserInput(Exception):
    pass
def create_tabs(tabs, key, chosen_notes, instrument):
    # Permutations of the notes in the chord
    # Creates all possible positions for the given notes (order is meaningful)
    for note_seq in itertools.permutations(chosen_notes):
        # Here we pick all distinct groups of strings size=length(note_seq) (order not important)
        for chosen_strings in itertools.combinations(instrument.strings_idx, len(note_seq)):
            # Permutations in the strings to fret
            all_fret_nrs = [ [ ] for i in range(len(note_seq))]
            for i in range(len(note_seq)):
                # Calculate all positions of a particular note on i-th string
                all_fret_nrs[i] = [ idx for idx in range(instrument.notes_per_string()) if note_seq[i] in instrument.note_at(chosen_strings[i],idx)]
                # breakpoint()
            for fret_nrs in itertools.product(*all_fret_nrs):
                # Create a tab for each combination of positions
                tab = Tab(note_seq,fret_nrs,chosen_strings, instrument.open_string_notes())
                tabs.add(key, tab)


def all_combinations(tabs, min_nr_notes, chord, instrument)-> None:
    # All chords from min nr notes=min_nr_notes to all notes given in input
    for nr_notes_in_chord in range(min_nr_notes,len(chord)+1):
        # breakpoint()
        # Here we pick all distinct groups of length notes_in_chord (order not important)
        for chosen_notes in itertools.combinations(chord, nr_notes_in_chord):
            key = f"{nr_notes_in_chord}_notes"
            create_tabs(tabs, key, chosen_notes, instrument)


def guided_combinations(tabs, chord, instrument)-> None:
    
    if len(chord) == 3:
        key = f"Triads"
        create_tabs(tabs, key, chord, instrument)
    elif len(chord) == 4:
        key = f"7th_Complete"
        create_tabs(tabs, key, chord, instrument)
        key = f"7th_No_Tonic"
        create_tabs(tabs, key, [chord[i] for i in range(len(chord)) if i!=0], instrument)
        key = f"7th_No_5th"
        create_tabs(tabs, key, [chord[i] for i in range(len(chord)) if i!=2], instrument)
    elif len(chord) == 5:
        key = f"9th_Complete"
        create_tabs(tabs, key, chord, instrument)
        key = f"9th_No_Tonic"
        create_tabs(tabs, key, [chord[i] for i in range(len(chord)) if i!=0], instrument)
        key = f"9th_No_5th"
        create_tabs(tabs, key, [chord[i] for i in range(len(chord)) if i!=2], instrument)
    elif len(chord) == 6:
        key = f"13th_No_Tonic"
        create_tabs(tabs, key, [chord[i] for i in range(len(chord)) if i!=0], instrument)
        key = f"13th_No_5th"
        create_tabs(tabs, key, [chord[i] for i in range(len(chord)) if i!=2], instrument)
        key = f"13th_No_Tonic_No_5th"
        create_tabs(tabs, key, [chord[i] for i in range(len(chord)) if (i!=0) and (i!=2)], instrument)


def main():

    user_chord = input("Enter chord (default C,E,G,Bb):")
    
    if user_chord != '':
        chord = user_chord.split(',')
    else:
        chord = ['C', 'E', 'G', 'Bb']

    min_nr_notes = input("Enter min nr of notes (default 3):")
    
    if min_nr_notes != '':
        min_nr_notes = int(min_nr_notes)
    else:
        min_nr_notes = 3
    
    print(f"chord is: {chord}")
    # breakpoint()

    instrument = Instrument('standard_acoustic_guitar')
    # breakpoint()
    
    tabs = Tabs(chord, instrument)
    all_combinations(tabs, min_nr_notes, chord, instrument)
    guided_combinations(tabs, chord, instrument)
    # breakpoint()
    params = {}
    
    try: 
        while True:      
            for param, data in Tab.inputs.items():
                while True:
                    try:
                        subtype = f" subtype {data['subtype']}," if 'subtype' in data else ""
                        wildcard = f" wildcard {data['wildcard']}," if 'wildcard' in data else ""
                        prompt = input(f"{data['desc']}, type {data['type']},{subtype}{wildcard} default {data['default']}: ")
                
                        if prompt == "q":
                            raise ExitFromUserInput()
                        
                        if prompt == '':
                            params[f'{param}'] = data['default']
                        else:
                            if data['type'] == tuple:
                                prompt = prompt.split(',')
                                # breakpoint()
                                params[param] =  data['type']([data['subtype'](i) for i in prompt])
                            elif data['type'] == bool:
                                if prompt != 'True' and prompt != 'False':
                                    raise ValueError()
                                params[param] = True if prompt == 'True' else False
                            else:
                                params[param] =  data['type'](prompt)
                        break
                    except ValueError:
                        print(f"Sorry, {prompt} cannot be assigned to {param} of type {data['type']}")
                        #better try again... Return to the start of the loop
                        continue
                    
            # breakpoint()
            if tabs.filter_tabs(**params):
                tabs.print_tabs()
    except ExitFromUserInput:
        print(f"Requested to exit, bye!!")
            
main()

        
            




from instrument import Instrument
from tab import Tabs


class ExitFromUserInput(Exception):
    pass


def main():

    DEFAULT_CHORD = ['C', 'E', 'G', 'Bb', 'D', 'F', 'A']
    while True:
        try:
            input_chord = input(f"Enter chord as 1st, 3rd, 5th, 7th, 9th, 11th, 13th, space to skip grade (default {DEFAULT_CHORD}):")
            
            if input_chord != '':
                chord = input_chord.split(',')
                if len(chord) != len(DEFAULT_CHORD):
                    raise Exception(f"Lenght of input chord is {len(chord)} instead of {len(DEFAULT_CHORD)}")
            else:
                chord = DEFAULT_CHORD
            break
        except Exception as e:
            print(e)
            print(f"Please enter again a chord of length {len(DEFAULT_CHORD)}")


    MIN_NR_NOTES = 2
    min_nr_notes = input(f"Enter min nr of notes (default {MIN_NR_NOTES}):")
    
    if min_nr_notes != '':
        min_nr_notes = int(min_nr_notes)
    else:
        min_nr_notes = MIN_NR_NOTES
    
    print(f"chord is: {chord}")
    # breakpoint()

    instrument = Instrument('standard_acoustic_guitar')
    # breakpoint()
    
    tabs = Tabs(chord, instrument, min_nr_notes)
    tabs.generate_tabs()
    # breakpoint()
    params = {}
    
    try: 
        while True:      
            for param, data in Tabs.inputs.items():
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

        
            



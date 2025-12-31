from globals import NOTES


instruments = {
    'standard_electric_guitar' : {
        'nr_strings' : 6,
        'lowest_note' : 'E',
        'frets_per_string': 22,
        'tuning_intervals' : [5,5,5,4,5],
    },
    'dropD_electric_guitar' : {
        'nr_strings' : 6,
        'lowest_note' : 'D',
        'frets_per_string': 22,
        'tuning_intervals' : [7,5,5,4,5],
    },
    'standard_acoustic_guitar' : {
        'nr_strings' : 6,
        'lowest_note' : 'E',
        'frets_per_string': 15,
        'tuning_intervals' : [5,5,5,4,5],
    }

}

class Instrument:
    '''
        Define the instrument, more specifically what notes are on each string
        Arrays are from the highest string to the lowest
    '''
    def __init__(self, name, nr_strings=None, lowest_note=None, frets_per_string=None, tuning_intervals=None):
        
        self.name = name

        self.nr_strings = nr_strings if nr_strings != None else instruments[f'{name}']['nr_strings']
        self.lowest_note = lowest_note if lowest_note != None else instruments[f'{name}']['lowest_note']
        # Playability
        self.frets_per_string = frets_per_string if frets_per_string != None else instruments[f'{name}']['frets_per_string']
        self.tuning_intervals = tuning_intervals if tuning_intervals != None else instruments[f'{name}']['tuning_intervals']

        if len(self.tuning_intervals) != self.nr_strings-1:
            raise Exception('Tuning intervals not compatible with nr strings')

        self.notes_on_string = [['x' for j in range(self.frets_per_string+1)] for i in range(self.nr_strings)]
        # breakpoint()
        idx_lowest = [i for i in range(len(NOTES)) if self.lowest_note in NOTES[i]][0]

        # String ids start from 1
        self.strings_idx = [i+1 for i in range(self.nr_strings)]

        # Assign the notes to each string
        for string in reversed(range(self.nr_strings)):
            # breakpoint()
            string_idx_reverse = self.nr_strings - string - 1
            chrom_int = 0
            for i in range(0,string_idx_reverse):
                chrom_int = chrom_int + self.tuning_intervals[i]
            idx_lowest_note = idx_lowest + ( chrom_int  % len(NOTES))
            
            self.notes_on_string[string] = [ NOTES[(idx_lowest_note+i)%len(NOTES)] for i in range(self.frets_per_string+1)]
        # breakpoint()

    def notes_per_string(self):
        return len(self.notes_on_string[0])

    def note_at(self, string_id, fret):
        return self.notes_on_string[string_id-1][fret]

    def open_string_notes(self):
        return [i[0] for i in self.notes_on_string]

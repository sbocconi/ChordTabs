NOTES_SHARP = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
NOTES_FLAT = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
# NOTES = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']
NOTES = [['B#','C'],['C#','Db'], ['D'],['D#','Eb'],['E','Fb'], ['E#','F'], ['F#','Gb'], ['G'], ['G#','Ab'], ['A'],['A#','Bb'],['B','Cb']]

TONIC = 0
THIRD = 1
FIFTH = 2
SEVENTH = 3
NINETH = 4
ELEVENTH = 5
THIRTEENTH = 6

DEGREES = {
            TONIC:"Tonic", 
            THIRD: "Third",
            FIFTH: "Fifth",
            SEVENTH: "Seventh",
            NINETH: "Nineth",
            ELEVENTH: "Eleventh",
            THIRTEENTH: "Thirteenth"
}

SEL_DEGREES = {
    "Triads" :
        {
            "Desc" : "All triads from the given chord",
            "Degrees" : [TONIC, THIRD, FIFTH]
        },
    "7th_Complete" :
        {
            "Desc" : "All complete 7th chords",
            "Degrees" : [TONIC, THIRD, FIFTH, SEVENTH]
        },
    "7th_No_Tonic":
        {
            "Desc" : "All 7th chords with no tonic",
            "Degrees" : [THIRD, FIFTH, SEVENTH]
        },
    "7th_No_5th":
        {
            "Desc" : "All 7th chords with no fifth",
            "Degrees" : [TONIC, THIRD, SEVENTH]
        },
    "7th_No_Tonic_No_5th":
        {
            "Desc" : "All 7th chords with no tonic and no fifth",
            "Degrees" : [THIRD, SEVENTH]
        },
    "9th_Complete":
        {
            "Desc" : "All complete 9th chords",
            "Degrees" : [TONIC, THIRD, FIFTH, SEVENTH, NINETH]
        },
    "9th_No_Tonic":
        {
            "Desc" : "All 9th chords with no tonic",
            "Degrees" : [THIRD, FIFTH, SEVENTH, NINETH]
        },
    "9th_No_5th":
        {
            "Desc" : "All 9th chords with no fifth",
            "Degrees" : [TONIC, THIRD, SEVENTH, NINETH]
        },
    "9th_No_Tonic_No_5th":
        {
            "Desc" : "All 9th chords with no tonic and no fifth",
            "Degrees" : [THIRD, SEVENTH, NINETH]
        },
    "11th_Complete":
        {
            "Desc" : "All complete 11th chords",
            "Degrees" : [TONIC, THIRD, FIFTH, SEVENTH, NINETH, ELEVENTH]
        },
    "11th_No_Tonic":
        {
            "Desc" : "All 11th chords with no tonic",
            "Degrees" : [THIRD, FIFTH, SEVENTH, NINETH, ELEVENTH]
        },
    "11th_No_5th":
        {
            "Desc" : "All 11th chords with no fifth",
            "Degrees" : [TONIC, THIRD, SEVENTH, NINETH, ELEVENTH]
        },
    "11th_No_Tonic_No_5th":
        {
            "Desc" : "All 11th chords with no tonic and no fifth",
            "Degrees" : [THIRD, SEVENTH, NINETH, ELEVENTH]
        },
    "11th_No_9th":
        {
            "Desc" : "All 11th chords without 9th",
            "Degrees" : [TONIC, THIRD, FIFTH, SEVENTH, ELEVENTH]
        },
    "11th_No_Tonic_No_9th":
        {
            "Desc" : "All 11th chords with no tonic and no 9th",
            "Degrees" : [THIRD, FIFTH, SEVENTH, ELEVENTH]
        },
    "11th_No_5th_No_9th":
        {
            "Desc" : "All 11th chords with no fifth and no 9th",
            "Degrees" : [TONIC, THIRD, SEVENTH, ELEVENTH]
        },
    "11th_No_Tonic_No_5th_No_9th":
        {
            "Desc" : "All 11th chords with no tonic, no fifth and no 9th",
            "Degrees" : [THIRD, SEVENTH, ELEVENTH]
        },
    "13th_Complete":
        {
            "Desc" : "All complete 13th chords",
            "Degrees" : [TONIC, THIRD, FIFTH, SEVENTH, NINETH, ELEVENTH, THIRTEENTH]
        },
    "13th_No_Tonic":
        {
            "Desc" : "All 13th chords with no tonic",
            "Degrees" : [THIRD, FIFTH, SEVENTH, NINETH, ELEVENTH, THIRTEENTH]
        },
    "13th_No_5th":
        {
            "Desc" : "All 13th chords with no fifth",
            "Degrees" : [TONIC, THIRD, SEVENTH, NINETH, ELEVENTH, THIRTEENTH]
        },
    "13th_No_Tonic_No_5th":
        {
            "Desc" : "All 13th chords with no tonic and no fifth",
            "Degrees" : [THIRD, SEVENTH, NINETH, ELEVENTH, THIRTEENTH]
        },
    "13th_No_9th":
        {
            "Desc" : "All 13th chords without 9th",
            "Degrees" : [TONIC, THIRD, FIFTH, SEVENTH, ELEVENTH, THIRTEENTH]
        },
    "13th_No_Tonic_No_9th":
        {
            "Desc" : "All 13th chords with no tonic and no 9th",
            "Degrees" : [THIRD, FIFTH, SEVENTH, ELEVENTH, THIRTEENTH]
        },
    "13th_No_5th_No_9th":
        {
            "Desc" : "All 13th chords with no fifth and no 9th",
            "Degrees" : [TONIC, THIRD, SEVENTH, ELEVENTH, THIRTEENTH]
        },
    "13th_No_Tonic_No_5th_No_9th":
        {
            "Desc" : "All 13th chords with no tonic, no fifth and no 9th",
            "Degrees" : [THIRD, SEVENTH, ELEVENTH, THIRTEENTH]
        },
    "13th_No_11th":
        {
            "Desc" : "All 13th chords without 11th",
            "Degrees" : [TONIC, THIRD, FIFTH, SEVENTH, NINETH, THIRTEENTH]
        },
    "13th_No_Tonic_No_11th":
        {
            "Desc" : "All 13th chords with no tonic and no 9th",
            "Degrees" : [THIRD, FIFTH, SEVENTH, NINETH, THIRTEENTH]
        },
    "13th_No_5th_No_11th":
        {
            "Desc" : "All 13th chords with no fifth and no 9th",
            "Degrees" : [TONIC, THIRD, SEVENTH, NINETH, THIRTEENTH]
        },
    "13th_No_Tonic_No_5th_No_11th":
        {
            "Desc" : "All 13th chords with no tonic, no fifth and no 9th",
            "Degrees" : [THIRD, SEVENTH, NINETH, THIRTEENTH]
        },
    "13th_No_9th_No_11th":
        {
            "Desc" : "All 13th chords with no 9th and no 11th",
            "Degrees" : [TONIC, THIRD, FIFTH, SEVENTH, THIRTEENTH]
        },
    "13th_No_Tonic_No_9th_No_11th":
        {
            "Desc" : "All 13th chords with no tonic, no 9th and no 11th",
            "Degrees" : [THIRD, FIFTH, SEVENTH, THIRTEENTH]
        },
    "13th_No_5th_No_9th_No_11th":
        {
            "Desc" : "All 13th chords with no fifth, no 9th and no 11th",
            "Degrees" : [TONIC, THIRD, SEVENTH, THIRTEENTH]
        },
    "13th_No_Tonic_No_5th_No_9th_No_11th":
        {
            "Desc" : "All 13th chords with no tonic, no fifth, no 9th and no 11th",
            "Degrees" : [THIRD, SEVENTH, THIRTEENTH]
        },
}


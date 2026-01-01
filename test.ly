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
    (dot-label-font-mag . 0.9)    ; label font size
  ))
  \column {
    "Chord with white labels in black dots"
    \fret-diagram-verbose #'( (place-fret 6 3 "G") (place-fret 5 1 "Bb") (place-fret 4 2 "E") (place-fret 3 5 "C") (mute 2) (mute 1) )
  }
}


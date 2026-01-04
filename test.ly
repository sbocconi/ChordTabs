\version "2.24.4"
\book {

\paper {
  #(set-paper-size "a4" 'portrait)
  
  top-margin = 5\mm
  bottom-margin = 6\mm
  % ragged-bottom If this is set to true, systems will be set at their natural spacing, neither compressed nor stretched vertically to fit the page.
  % ragged-last-bottom If this is set to false, then the last page, and the last page in each section created with a \bookpart block, will be vertically justified in the same way as the earlier pages.

  %left-margin = 10\mm % The margin between the left edge of the page and the start of the staff lines in unindented systems. If the paper size is modified, this dimension’s default value is scaled accordingly. If left-margin is unset, and both line-width and right-margin are set, then left-margin is set to (paper-width - line-width - right-margin). If only line-width is set, then both margins are set to ((paper-width - line-width) / 2), and the systems are consequently centered on the page. Also see check-consistency.
  %right-margin = 10\mm % The margin between the right edge of the page and the end of the staff lines in non-ragged systems. If the paper size is modified, this dimension’s default value is scaled accordingly. If right-margin is unset, and both line-width and left-margin are set, then right-margin is set to (paper-width - line-width - left-margin). If only line-width is set, then both margins are set to ((paper-width - line-width) / 2), and the systems are consequently centered on the page.
  %line-width = 170\mm leave unset to have line-width = (paper-width - left-margin - right-margin)
  
  check-consistency = ##t %If this is true (the default value), print a warning if left-margin, line-width, and right-margin do not exactly add up to paper-width, and replace each of these (except paper-width) with their default values (scaled to the paper size if necessary). If set to false, ignore any inconsistencies and allow systems to run off the edge of the page. 
  
  two-sided = ##f % If set to true, use inner-margin, outer-margin and binding-offset to determine margins depending on whether the page number is odd or even. This overrides left-margin and right-margin.
  
  tocItemMarkup = \tocItemWithDotsMarkup
}

\header {
  title = "SUITE I."
  composer = "J. S. Bach."
}

\markuplist \table-of-contents
\pageBreak

\tocItem \markup "Tabs for the chord: ['C', 'E', 'G', 'Bb', 'D', 'F', 'A']"
\markuplist {
\override #'(fret-diagram-details . (
    (finger-code . in-dot)
    (dot-color . black)
    (dot-label-color . white)
    (dot-radius . 0.55)
    (dot-label-font-mag . 0.8)
    (string-count . 6)
    (fret-count . 5)
  ))

  {
  \fontsize #4 \bold "Tabs for the chord: ['C', 'E', 'G', 'Bb', 'D', 'F', 'A']"
  \vspace #1
  \fontsize #1 \italic {
    \wordwrap-string "Generated automatically by Farback"
  }
  \vspace #1
  \fontsize #3 \bold "Automatically Wrapped Fretboard Diagrams"
  \vspace #3

    \fill-line {
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 8 "F")
          (place-fret 4 8 "Bb") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 6 "Bb") (place-fret 5 8 "F")
          (place-fret 4 7 "A") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 10 "D") (place-fret 5 12 "A")
          (place-fret 4 8 "Bb") (place-fret 3 10 "F")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 13 "F") (place-fret 5 12 "A")
          (place-fret 4 12 "D") (place-fret 3 15 "Bb")
          (place-fret 2 13 "C") (place-fret 1 15 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
    }
    \vspace #3

    \fill-line {
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 8 "F")
          (place-fret 4 8 "Bb") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 6 "Bb") (place-fret 5 8 "F")
          (place-fret 4 7 "A") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 10 "D") (place-fret 5 12 "A")
          (place-fret 4 8 "Bb") (place-fret 3 10 "F")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 13 "F") (place-fret 5 12 "A")
          (place-fret 4 12 "D") (place-fret 3 15 "Bb")
          (place-fret 2 13 "C") (place-fret 1 15 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
    }
    \vspace #3
    \fill-line {
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 8 "F")
          (place-fret 4 8 "Bb") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 6 "Bb") (place-fret 5 8 "F")
          (place-fret 4 7 "A") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 10 "D") (place-fret 5 12 "A")
          (place-fret 4 8 "Bb") (place-fret 3 10 "F")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 13 "F") (place-fret 5 12 "A")
          (place-fret 4 12 "D") (place-fret 3 15 "Bb")
          (place-fret 2 13 "C") (place-fret 1 15 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
    }
    \vspace #3
    \fill-line {
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 8 "F")
          (place-fret 4 8 "Bb") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 6 "Bb") (place-fret 5 8 "F")
          (place-fret 4 7 "A") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 10 "D") (place-fret 5 12 "A")
          (place-fret 4 8 "Bb") (place-fret 3 10 "F")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 13 "F") (place-fret 5 12 "A")
          (place-fret 4 12 "D") (place-fret 3 15 "Bb")
          (place-fret 2 13 "C") (place-fret 1 15 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
    }
    \vspace #3
    \fill-line {
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 8 "F")
          (place-fret 4 8 "Bb") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 6 "Bb") (place-fret 5 8 "F")
          (place-fret 4 7 "A") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 10 "D") (place-fret 5 12 "A")
          (place-fret 4 8 "Bb") (place-fret 3 10 "F")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 13 "F") (place-fret 5 12 "A")
          (place-fret 4 12 "D") (place-fret 3 15 "Bb")
          (place-fret 2 13 "C") (place-fret 1 15 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
    }
    \vspace #3
    \fill-line {
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 8 "F")
          (place-fret 4 8 "Bb") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 6 "Bb") (place-fret 5 8 "F")
          (place-fret 4 7 "A") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 10 "D") (place-fret 5 12 "A")
          (place-fret 4 8 "Bb") (place-fret 3 10 "F")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 13 "F") (place-fret 5 12 "A")
          (place-fret 4 12 "D") (place-fret 3 15 "Bb")
          (place-fret 2 13 "C") (place-fret 1 15 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
    }
    \vspace #3
    \fill-line {
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 8 "F")
          (place-fret 4 8 "Bb") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 6 "Bb") (place-fret 5 8 "F")
          (place-fret 4 7 "A") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 10 "D") (place-fret 5 12 "A")
          (place-fret 4 8 "Bb") (place-fret 3 10 "F")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 13 "F") (place-fret 5 12 "A")
          (place-fret 4 12 "D") (place-fret 3 15 "Bb")
          (place-fret 2 13 "C") (place-fret 1 15 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
    }
    \vspace #3
    \fill-line {
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 8 "F")
          (place-fret 4 8 "Bb") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 6 "Bb") (place-fret 5 8 "F")
          (place-fret 4 7 "A") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 10 "D") (place-fret 5 12 "A")
          (place-fret 4 8 "Bb") (place-fret 3 10 "F")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 13 "F") (place-fret 5 12 "A")
          (place-fret 4 12 "D") (place-fret 3 15 "Bb")
          (place-fret 2 13 "C") (place-fret 1 15 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
    }
    \vspace #3
    \fill-line {
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 8 "F")
          (place-fret 4 8 "Bb") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 6 "Bb") (place-fret 5 8 "F")
          (place-fret 4 7 "A") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 10 "D") (place-fret 5 12 "A")
          (place-fret 4 8 "Bb") (place-fret 3 10 "F")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 13 "F") (place-fret 5 12 "A")
          (place-fret 4 12 "D") (place-fret 3 15 "Bb")
          (place-fret 2 13 "C") (place-fret 1 15 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
    }
    \vspace #3
    \fill-line {
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 8 "F")
          (place-fret 4 8 "Bb") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 6 "Bb") (place-fret 5 8 "F")
          (place-fret 4 7 "A") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 10 "D") (place-fret 5 12 "A")
          (place-fret 4 8 "Bb") (place-fret 3 10 "F")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 13 "F") (place-fret 5 12 "A")
          (place-fret 4 12 "D") (place-fret 3 15 "Bb")
          (place-fret 2 13 "C") (place-fret 1 15 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
    }
    \vspace #3



  }
}
\tocItem \markup "Tabs for the chord: ['C', 'E', 'G', 'Bb', 'D', 'F', 'A']"
\markuplist {
\override #'(fret-diagram-details . (
    (finger-code . in-dot)
    (dot-color . black)
    (dot-label-color . white)
    (dot-radius . 0.55)
    (dot-label-font-mag . 0.8)
    (string-count . 6)
    (fret-count . 5)
  ))

  {
  \fontsize #4 \bold "Tabs for the chord: ['C', 'E', 'G', 'Bb', 'D', 'F', 'A']"
  \vspace #1
  \fontsize #1 \italic {
    \wordwrap-string "Generated automatically by Farback"
  }
  \vspace #1
  \fontsize #3 \bold "Automatically Wrapped Fretboard Diagrams"
  \vspace #3

    \fill-line {
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 8 "F")
          (place-fret 4 8 "Bb") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 6 "Bb") (place-fret 5 8 "F")
          (place-fret 4 7 "A") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 10 "D") (place-fret 5 12 "A")
          (place-fret 4 8 "Bb") (place-fret 3 10 "F")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 13 "F") (place-fret 5 12 "A")
          (place-fret 4 12 "D") (place-fret 3 15 "Bb")
          (place-fret 2 13 "C") (place-fret 1 15 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
    }
    \vspace #3

    \fill-line {
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 8 "F")
          (place-fret 4 8 "Bb") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 6 "Bb") (place-fret 5 8 "F")
          (place-fret 4 7 "A") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 10 "D") (place-fret 5 12 "A")
          (place-fret 4 8 "Bb") (place-fret 3 10 "F")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 13 "F") (place-fret 5 12 "A")
          (place-fret 4 12 "D") (place-fret 3 15 "Bb")
          (place-fret 2 13 "C") (place-fret 1 15 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
    }
    \vspace #3
    \fill-line {
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 8 "F")
          (place-fret 4 8 "Bb") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 6 "Bb") (place-fret 5 8 "F")
          (place-fret 4 7 "A") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 10 "D") (place-fret 5 12 "A")
          (place-fret 4 8 "Bb") (place-fret 3 10 "F")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 13 "F") (place-fret 5 12 "A")
          (place-fret 4 12 "D") (place-fret 3 15 "Bb")
          (place-fret 2 13 "C") (place-fret 1 15 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
    }
    \vspace #3
    \fill-line {
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 8 "F")
          (place-fret 4 8 "Bb") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 6 "Bb") (place-fret 5 8 "F")
          (place-fret 4 7 "A") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 10 "D") (place-fret 5 12 "A")
          (place-fret 4 8 "Bb") (place-fret 3 10 "F")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 13 "F") (place-fret 5 12 "A")
          (place-fret 4 12 "D") (place-fret 3 15 "Bb")
          (place-fret 2 13 "C") (place-fret 1 15 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
    }
    \vspace #3
    \fill-line {
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 8 "F")
          (place-fret 4 8 "Bb") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 6 "Bb") (place-fret 5 8 "F")
          (place-fret 4 7 "A") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 10 "D") (place-fret 5 12 "A")
          (place-fret 4 8 "Bb") (place-fret 3 10 "F")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 13 "F") (place-fret 5 12 "A")
          (place-fret 4 12 "D") (place-fret 3 15 "Bb")
          (place-fret 2 13 "C") (place-fret 1 15 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
    }
    \vspace #3
    \fill-line {
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 8 "F")
          (place-fret 4 8 "Bb") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 6 "Bb") (place-fret 5 8 "F")
          (place-fret 4 7 "A") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 10 "D") (place-fret 5 12 "A")
          (place-fret 4 8 "Bb") (place-fret 3 10 "F")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 13 "F") (place-fret 5 12 "A")
          (place-fret 4 12 "D") (place-fret 3 15 "Bb")
          (place-fret 2 13 "C") (place-fret 1 15 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
    }
    \vspace #3
    \fill-line {
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 8 "F")
          (place-fret 4 8 "Bb") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 6 "Bb") (place-fret 5 8 "F")
          (place-fret 4 7 "A") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 10 "D") (place-fret 5 12 "A")
          (place-fret 4 8 "Bb") (place-fret 3 10 "F")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 13 "F") (place-fret 5 12 "A")
          (place-fret 4 12 "D") (place-fret 3 15 "Bb")
          (place-fret 2 13 "C") (place-fret 1 15 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
    }
    \vspace #3
    \fill-line {
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 8 "F")
          (place-fret 4 8 "Bb") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 6 "Bb") (place-fret 5 8 "F")
          (place-fret 4 7 "A") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 10 "D") (place-fret 5 12 "A")
          (place-fret 4 8 "Bb") (place-fret 3 10 "F")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 13 "F") (place-fret 5 12 "A")
          (place-fret 4 12 "D") (place-fret 3 15 "Bb")
          (place-fret 2 13 "C") (place-fret 1 15 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
    }
    \vspace #3
    \fill-line {
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 8 "F")
          (place-fret 4 8 "Bb") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 6 "Bb") (place-fret 5 8 "F")
          (place-fret 4 7 "A") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 10 "D") (place-fret 5 12 "A")
          (place-fret 4 8 "Bb") (place-fret 3 10 "F")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 13 "F") (place-fret 5 12 "A")
          (place-fret 4 12 "D") (place-fret 3 15 "Bb")
          (place-fret 2 13 "C") (place-fret 1 15 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
    }
    \vspace #3
    \fill-line {
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 8 "F")
          (place-fret 4 8 "Bb") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 6 "Bb") (place-fret 5 8 "F")
          (place-fret 4 7 "A") (place-fret 3 7 "D")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 10 "D") (place-fret 5 12 "A")
          (place-fret 4 8 "Bb") (place-fret 3 10 "F")
          (place-fret 2 8 "G") (place-fret 1 8 "C")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 13 "F") (place-fret 5 12 "A")
          (place-fret 4 12 "D") (place-fret 3 15 "Bb")
          (place-fret 2 13 "C") (place-fret 1 15 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
      \hspace #3
      \scale #'(1.4 . 1.4) {
        \fret-diagram-verbose #'(
          (place-fret 6 5 "A") (place-fret 5 5 "D")
          (place-fret 4 3 "F") (place-fret 3 3 "Bb")
          (place-fret 2 1 "C") (place-fret 1 3 "G")
        )
      }
    }
    \vspace #3

  }
}
}

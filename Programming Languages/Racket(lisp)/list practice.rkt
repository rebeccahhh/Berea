#lang racket
(require test-engine/racket-tests)

;; List Practice
;;  Template for problems:
;;  (define (fun ls)
;;    (cond 
;;      [(empty? ls) ...]
;;      [else
;;        ... (first ls) ...
;;        ... (fun (rest ls)) ...
;;       ]))
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 1. Define a function called *sum-all* that consumes a list of numbers 
;; and returns the sum of all of the numbers in the list.
(define (sum-all lon)
  (cond
    [(empty? lon) 0]
    [else
     (+ (first lon) (sum-all (rest lon)))
    ]
  )
)
(check-expect (sum-all '(1 2 3)) 6)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 2. Define a function called *sum-odd* that consumes a list of numbers 
;; and returns the sum of all of the odd numbers in the list.
;; HINT: This (and other functions) may need another 'cond' in the
;; else clause, so you can inspect the value of (first lon) and decide
;; what to do.
(define (sum-odd lon)
  (cond
    [(empty? lon) 0]
    [else
     (+ (first (filter odd? lon)) (sum-odd (rest (filter odd? lon))))
     ]
   )
)
(check-expect (sum-odd '(1 2 3 4 5)) 9)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 3. Define a function called total-lengths that consumes a 
;; list of strings and returns the length of all of the strings
;; in the list.
(define (total-lengths los)
  (cond
    [(empty? los) 0]
    [else
     (+ (string-length (first los)) (total-lengths (rest los)))
    ]
  )
)
(check-expect (total-lengths '("dog" "fish" "aardvark")) 15)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4. Define a function fcalled bop (short for "balance of power") that
;; takes a list of coin flips and returns the difference in the number
;; of flips that were heads vs. tails. Heads are +1, tails are -1. For example:
;; 
;; (bop '(heads tails heads))
;; would return 1, because there were two 'heads and one 'tails, while
;;
;; (bop '(heads heads heads tails))
;; would return 2, because there were three heads and one tails.
;;
;;
;; This problem introduces symbols. A symbol looks like a string,
;; but is really a single value. They have no length, no parts.
;;
;; (equal? "heads" 'heads) is false.
;; (equal? 'heads 'heads) is true.
;; (symbol? "heads") is false.
;; (symbol? 'heads) is true.
;;
;; '("heads" "tails") is a list of strings.
;; '(heads tails) is a list of symbols.

(define (bop ls)
  (cond
    [(empty? ls) 0]
    [else
     (+
       (cond
         [(equal? 'heads (first ls)) 1]
         [(equal? 'tails (first ls)) -1]
        )
        (bop (rest ls))
      )
    ]
  )
)

(check-expect (bop '(heads tails heads)) 1)
(check-expect (bop '(heads tails tails)) -1)
(check-expect (bop '(heads heads heads tails)) 2)
(check-expect (bop '(heads heads heads heads)) 4)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 5. Define a function called "tlas" that consumes a list
;; of strings and returns a list containing only the strings
;; that are of length three. These are Three Letter Acroynms.
;; HINT: You'll need cons for this.

(define (tlas ls n)
  (cond
    [(empty? ls) '()]
    [else
     (cond
      [(equal? n (string-length (first ls))) (cons (first ls) (tlas (rest ls) n))]
      [else
       (tlas (rest ls) n)
      ]
      )
    ]
  )
)
 
(check-expect (tlas '("TWA" "IBM" "GOOGLE" "MCJ") 3)
              '("TWA" "IBM" "MCJ"))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 6. Define a function called only-odds that consumes a list
;; of numbers and returns a list containing only the odd numbers.

(define (only-odds ls)
  (cond
    [(empty? ls) '()]
    [else
     (cond
       [(odd? (first ls)) (cons (first ls) (only-odds (rest ls)))]
       [else
        (only-odds (rest ls))
       ]
     )
    ]
  )
)
(check-expect (only-odds '(1 2 3 4 5)) '(1 3 5))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 7. Define a function called first-odd that returns the first
;; odd number found in a list. If no odds are found, it returns -1.

(define (first-odd ls)
  (cond
    [(empty? ls) 0]
    [else
     (first (only-odds ls))
    ]
  )
)

(check-expect (first-odd '(2 4 6 8 9 10 11)) 9)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 8. Define a function called "filter". It consumes a predicate
;; and a list, and it returns a list of all the elements that 
;; satisfy that predicate.

;; I had to change the name, becuase it rewrote the filter function for the whole file.
(define (filterer pred? ls)
  (cond
    [(empty? ls) 0]
    [else
     (filter pred? ls)]
  )
)
(check-expect (filterer odd? '(1 2 3 4 5)) '(1 3 5))
(check-expect (filterer even? '(1 2 3 4 5)) '(2 4))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 9. Define a function called "first-that-is". It consumes
;; a predicate and a list, and returns the first element that 
;; satisfies that predicate. It should return false
;; if nothing is found.

(define (first-that-is pred? ls)
  (cond
    [(empty? ls) 0]
    [else
     (first(filter pred? ls))
    ]
  )
)
(check-expect (first-that-is odd? '(2 4 6 7 9 10)) 7)
(check-expect (first-that-is even? '(2 4 6 7 9 10)) 2)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 10. Define a function called "lon->number". It should consume
;; a list of numbers, and treat each number as if it was a digit
;; in a single number. For example, '(1 2 3) should become
;; 123, and '(2 4 6 8) should become 2468.

(define (lon->number ls)
  (cond
    [(empty? ls) 0]
    [else
     (string->number
     (string-append (number->string(first ls))
                     (cond
                       [(empty? (rest ls)) ""]
                       [else
                        (number->string (lon->number (rest ls)))
                       ]
                      )
      )
     )
    ]
  )
)

(check-expect (lon->number '(1 2 3)) 123)
(check-expect (lon->number '(2 4 6 8)) 2468)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 11. Define a function called "sum-mixed-odds". Using functions
;; you have previously defined (and, therefore, breaking the template),
;; it should only sum odd numbers in a list of mixed data. I believe
;; this is solved by using two functions you have already defined.

(define (sum-mixed-odds ls)
  (cond
    [(empty? ls) 0]
    [else
     (sum-all (only-odds (filter number? ls)))]
  )
)
(check-expect (sum-mixed-odds '(1 "two" three 4 5 "six" 7)) 13)
(check-expect (sum-mixed-odds '(2 "three" 4 6 "eight")) 0)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 12. Define a function called lookup. It takes a symbol and a list
;; of lists. It should return the second element of a sublist if 
;; the symbol matches the first element of a sublist.
;;
;; For example
;;
;; (lookup 'matt '((simon 1) (matthew 5) (matt 39)))
;;
;; should return 39. While it appears to break the template, it doesn't.
;; 
;; Failure to find the symbol should return false.

(define (lookup key lols)
  (cond
    [(empty? lols) #f]
    [else
     (cond
       [(equal? key (first (first lols))) (second (first lols))]
       [else
        (lookup key (rest lols))
       ]
      )
     ]
   )
)
(check-expect (lookup 'matt '((simon 1) (matthew 5) (matt 39))) 39)
(check-expect (lookup 'simon '((simon 1) (matthew 5) (matt 39))) 1)

(test)
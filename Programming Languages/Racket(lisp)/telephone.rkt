#lang racket
(require test-engine/racket-tests)

;; The number-to-letter map.
(define keypad
  (hash 0 '()
        1 '()
        2 '("A" "B" "C")
        3 '("D" "E" "F")
        4 '("G" "H" "I")
        5 '("J" "K" "L")
        6 '("M" "N" "O")
        7 '("P" "Q" "R" "S")
        8 '("T" "U" "V")
        9 '("W" "X" "Y" "Z")
        ))

(define (get-list-of-letters n)
  (hash-ref keypad n))




;; CONTRACT
;; number->list-of-numbers : number -> list-of-numbers
;; PURPOSE
;; Takes a number and returns that number broken into
;; a list by tens places. For example,
;; 123 becomes '(1 2 3). Note odd construction of recursion
;; so that the number comes out in-order.
(define (number->list-of-numbers n)
  (cond
    [(zero? (quotient n 10)) (list n)]
    [else
     (append (number->list-of-numbers (quotient n 10))
             (list (remainder n 10)))
     ]))

(check-expect(number->list-of-numbers 32) '(3 2))
(check-expect(number->list-of-numbers 5) '(5))




;; CONTRACT
;; lon->lol : list-of numbers -> list-of numbers
;; PURPOSE
;; Takes a list of numbers and returns all the letter lists
;; that map to those numbers. For example, the list
;; '(2 3) returns '(("A" "B" "C") ("D" "E" "F"))
(define (lon->lol lon)
  (cond
    [(empty? lon) '()]
    [else
     (define letters (get-list-of-letters (first lon)))
     (cond
       [(empty? letters)
        (lon->lol (rest lon))]
       [else (cons letters
                   (lon->lol (rest lon)))])
     ]))

(check-expect(lon->lol (number->list-of-numbers 32)) '(("D" "E" "F") ("A" "B" "C")))
(check-expect(lon->lol (number->list-of-numbers 523)) '(("J" "K" "L") ("A" "B" "C") ("D" "E" "F")))



;; CONTRACT
;; glue : string list-of-string -> list-of-string
;;
(define (glue n lis)
  (cond
    [(empty? lis)]
    [else
     (map (lambda (element) (string-append n element)) lis)
     ]
    )
  )

(check-expect (glue "A" '("B" "C")) '("AB" "AC"))
(check-expect (glue "A" '("B" "C" "D" "J")) '("AB" "AC" "AD" "AJ"))


;; CONTRACT
;; super-glue : string list-of-string -> list-of-string
;; 
(define (super-glue list1 list2)
  (cond
    [(empty? list1) '()]
    [else
     (cond
       [(empty? list2) '()]
       [else
        (append (glue (first list1) list2) (super-glue (rest list1) list2))
        ]
       )
     ]
    )
  )
(check-expect (super-glue '("A" "B") '("C" "D")) '("AC" "AD" "BC" "BD"))
(check-expect (super-glue '("A" "B" "C") '("D" "E" "F")) '("AD" "AE" "AF" "BD" "BE" "BF" "CD" "CE" "CF"))


;; CONTRACT
;; gorilla-glue : list-of-lists
(define (gorilla-glue ls)
  (cond
    [(empty? ls) '()]
    [else
     (super-glue (first ls) (second ls))
     (cond
       [(empty? (rest (rest ls))) (super-glue (first ls) (second ls))]
       [else
        (gorilla-glue (append (list (super-glue (first ls) (second ls))) (rest (rest ls))))
       ]
    )
   ]
  )
)
(check-expect (gorilla-glue '(("A" "B") ("C" "D") ("E" "F"))) '("ACE" "ACF" "ADE" "ADF" "BCE" "BCF" "BDE" "BDF"))
(check-expect (gorilla-glue '(("AC" "AD" "BC" "BD") ("E" "F"))) '("ACE" "ACF" "ADE" "ADF" "BCE" "BCF" "BDE" "BDF"))

;; CONTRACT
;; gaga : number -> list-of strings
;; Takes a number and returns all possible letter combinations
;; from a numeric keypad. For example,
;; 8675309 returns 1296 results.
;; NOTE: The function gaga skips the numbers 0 and 1, because
;; no letters live there.
(define (gaga n)
  (gorilla-glue
   (lon->lol
   (number->list-of-numbers n))))

(check-expect (gaga 32) '("DA" "DB" "DC" "EA" "EB" "EC" "FA" "FB" "FC"))
(check-expect (gaga 123457) '("ADGJP" "ADGJQ" "ADGJR" "ADGJS" "ADGKP" "ADGKQ" "ADGKR" "ADGKS" "ADGLP" "ADGLQ" "ADGLR" "ADGLS"
  "ADHJP" "ADHJQ" "ADHJR" "ADHJS" "ADHKP" "ADHKQ" "ADHKR" "ADHKS" "ADHLP" "ADHLQ" "ADHLR" "ADHLS" "ADIJP" "ADIJQ" "ADIJR" "ADIJS"
  "ADIKP" "ADIKQ" "ADIKR" "ADIKS" "ADILP" "ADILQ" "ADILR" "ADILS" "AEGJP" "AEGJQ" "AEGJR" "AEGJS" "AEGKP" "AEGKQ" "AEGKR" "AEGKS"
  "AEGLP" "AEGLQ" "AEGLR" "AEGLS" "AEHJP" "AEHJQ" "AEHJR" "AEHJS" "AEHKP" "AEHKQ" "AEHKR" "AEHKS" "AEHLP" "AEHLQ" "AEHLR" "AEHLS"
  "AEIJP" "AEIJQ" "AEIJR" "AEIJS" "AEIKP" "AEIKQ" "AEIKR" "AEIKS" "AEILP" "AEILQ" "AEILR" "AEILS" "AFGJP" "AFGJQ" "AFGJR" "AFGJS"
  "AFGKP" "AFGKQ" "AFGKR" "AFGKS" "AFGLP" "AFGLQ" "AFGLR" "AFGLS" "AFHJP" "AFHJQ" "AFHJR" "AFHJS" "AFHKP" "AFHKQ" "AFHKR" "AFHKS"
  "AFHLP" "AFHLQ" "AFHLR" "AFHLS" "AFIJP" "AFIJQ" "AFIJR" "AFIJS" "AFIKP" "AFIKQ" "AFIKR" "AFIKS" "AFILP" "AFILQ" "AFILR" "AFILS"
  "BDGJP" "BDGJQ" "BDGJR" "BDGJS" "BDGKP" "BDGKQ" "BDGKR" "BDGKS" "BDGLP" "BDGLQ" "BDGLR" "BDGLS" "BDHJP" "BDHJQ" "BDHJR" "BDHJS"
  "BDHKP" "BDHKQ" "BDHKR" "BDHKS" "BDHLP" "BDHLQ" "BDHLR" "BDHLS" "BDIJP" "BDIJQ" "BDIJR" "BDIJS" "BDIKP" "BDIKQ" "BDIKR" "BDIKS"
  "BDILP" "BDILQ" "BDILR" "BDILS" "BEGJP" "BEGJQ" "BEGJR" "BEGJS" "BEGKP" "BEGKQ" "BEGKR" "BEGKS" "BEGLP" "BEGLQ" "BEGLR" "BEGLS"
  "BEHJP" "BEHJQ" "BEHJR" "BEHJS" "BEHKP" "BEHKQ" "BEHKR" "BEHKS" "BEHLP" "BEHLQ" "BEHLR" "BEHLS" "BEIJP" "BEIJQ" "BEIJR" "BEIJS"
  "BEIKP" "BEIKQ" "BEIKR" "BEIKS" "BEILP" "BEILQ" "BEILR" "BEILS" "BFGJP" "BFGJQ" "BFGJR" "BFGJS" "BFGKP" "BFGKQ" "BFGKR" "BFGKS"
  "BFGLP" "BFGLQ" "BFGLR" "BFGLS" "BFHJP" "BFHJQ" "BFHJR" "BFHJS" "BFHKP" "BFHKQ" "BFHKR" "BFHKS" "BFHLP" "BFHLQ" "BFHLR" "BFHLS"
  "BFIJP" "BFIJQ" "BFIJR" "BFIJS" "BFIKP" "BFIKQ" "BFIKR" "BFIKS" "BFILP" "BFILQ" "BFILR" "BFILS" "CDGJP" "CDGJQ" "CDGJR" "CDGJS"
  "CDGKP" "CDGKQ" "CDGKR" "CDGKS" "CDGLP" "CDGLQ" "CDGLR" "CDGLS" "CDHJP" "CDHJQ" "CDHJR" "CDHJS" "CDHKP" "CDHKQ" "CDHKR" "CDHKS"
  "CDHLP" "CDHLQ" "CDHLR" "CDHLS" "CDIJP" "CDIJQ" "CDIJR" "CDIJS" "CDIKP" "CDIKQ" "CDIKR" "CDIKS" "CDILP" "CDILQ" "CDILR" "CDILS"
  "CEGJP" "CEGJQ" "CEGJR" "CEGJS" "CEGKP" "CEGKQ" "CEGKR" "CEGKS" "CEGLP" "CEGLQ" "CEGLR" "CEGLS" "CEHJP" "CEHJQ" "CEHJR" "CEHJS"
  "CEHKP" "CEHKQ" "CEHKR" "CEHKS" "CEHLP" "CEHLQ" "CEHLR" "CEHLS" "CEIJP" "CEIJQ" "CEIJR" "CEIJS" "CEIKP" "CEIKQ" "CEIKR" "CEIKS"
  "CEILP" "CEILQ" "CEILR" "CEILS" "CFGJP" "CFGJQ" "CFGJR" "CFGJS" "CFGKP" "CFGKQ" "CFGKR" "CFGKS" "CFGLP" "CFGLQ" "CFGLR" "CFGLS"
  "CFHJP" "CFHJQ" "CFHJR" "CFHJS" "CFHKP" "CFHKQ" "CFHKR" "CFHKS" "CFHLP" "CFHLQ" "CFHLR" "CFHLS" "CFIJP" "CFIJQ" "CFIJR" "CFIJS"
  "CFIKP" "CFIKQ" "CFIKR" "CFIKS" "CFILP" "CFILQ" "CFILR" "CFILS"))

(test)
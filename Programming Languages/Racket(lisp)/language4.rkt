#lang racket
(require test-engine/racket-tests)

(struct DP (left right))
;;math
(define eins '(DASPLUS 3 5))
(define zwei '(DASPLUS 0 -1))
(define drei '(DASMAL 2 3))
(define vier '(DASGETEILT 6 3))
(define fünf '(DASMINUS (DASMAL 2 3) 3))
(define sechs '(DASMINUS 5 3))
(define sieben '(DASMAL (DASMAL 2 1) (DASMAL 1 3)))
(define acht '(DASMINUS 5 3))
;;ob0
(define nuen '{ob0 (DASPLUS 1 2) 8 -1} ) ;;changed because everything should always evaluate to 8

(struct structplus (left right) #:transparent)
(struct structminus (left right) #:transparent)
(struct structmal (left right) #:transparent) ;;multiply
(struct structgeteilt (left right) #:transparent) ;;divide
(struct structob (expression false true) #:transparent)

;;CONTRACT
;; ob0 : number -> number
;;check if the number is 0, return numeric versions of True and False
(define (ob0 expression true false) ;;ob is if in German...
  (cond
    [(equal? 0 (interp expression)) false] ;; this will return 8, becausee it should.
    [else true]
  )
)

;; CONTRACT
;; parse : concrete-syntax -> abstract-syntax
;; take the info from program-# and change it's syntax
(define (parse concrete)
  (cond
    ;;check if it's already a number, if it is, return that
    [(number? concrete) concrete]
    ;;check if its addition, subtraction, multiplication, and division.
    [(equal? (first concrete) 'DASPLUS) (structplus (parse(second concrete)) (parse(third concrete)))]
    [(equal? (first concrete) 'DASMINUS) (structminus (parse (second concrete)) (parse(third concrete)))]
    [(equal? (first concrete) 'DASMAL) (structmal (parse(second concrete)) (parse(third concrete)))]
    [(equal? (first concrete) 'DASGETEILT) (structgeteilt (parse(second concrete)) (parse(third concrete)))]
    [(equal? (first concrete) 'ob0) (ob0 (parse(second concrete)) (third concrete) (third (rest concrete)))]
    [else
     (error 'parse "Syntax Error in ~a." concrete)]
  )
)

;; CONTRACT
;; interp : abstract-syntax -> number
;; take the info from parse, and interpret it so that it can be computed.
(define (interp abstract)
  (cond
    ;;check if it's a number, if it is, return that
    [(number? abstract) abstract]
    ;;check if it's an addion, subtraction, multiplication, or division structure, then do the appropriate action
    [(structplus? abstract)
     (+ (interp(structplus-left abstract))
     (interp(structplus-right abstract)))]
    [(structminus? abstract)
     (- (interp(structminus-left abstract))
     (interp(structminus-right abstract)))]
    [(structmal? abstract)
     (* (interp(structmal-left abstract))
     (interp(structmal-right abstract)))]
    [(structgeteilt? abstract)
     (/ (interp(structgeteilt-left abstract))
     (interp(structgeteilt-right abstract)))]
    [else
     "interpreter error"]
   )
)


(check-expect (interp (parse eins)) 8)
(check-expect (interp (parse drei)) -1)
(check-expect (interp (parse zwei)) 6)
(check-expect (interp (parse vier)) 2)
(check-expect (interp (parse fünf)) 3)
(check-expect (interp (parse sechs)) 2)
(check-expect (interp (parse seiben)) 6)
(check-expect (interp (parse acht)) 2)
(check-expect (parse neun) 8) ;;ob0


(test)
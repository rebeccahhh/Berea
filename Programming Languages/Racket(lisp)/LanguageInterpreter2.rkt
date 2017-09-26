#lang racket
(require test-engine/racket-tests)

(struct DP (left right))

(define program-one '(DASPLUS 3 5))
(define program-two '(DASPLUS 0 -1))
(define program-three '(DASMAL 2 3))
(define program-four '(DASGETEILT 6 3))


(struct structplus (left right) #:transparent)
(struct structminus (left right) #:transparent)
(struct structmal (left right) #:transparent) ;;multiply
(struct structgeteilt (left right) #:transparent) ;;divide

;; CONTRACT
;; parse : concrete-syntax -> abstract-syntax
;; take the info from program-one and change it's syntax
(define (parse concrete)
  (cond
    [(equal? (first concrete) 'DASPLUS) (structplus (second concrete) (third concrete))]
    [(equal? (first concrete) 'DASMINUS) (structminus (second concrete) (third concrete))]
    [(equal? (first concrete) 'DASMAL) (structmal (second concrete) (third concrete))]
    [(equal? (first concrete) 'DASGETEILT) (structgeteilt (second concrete) (third concrete))]
    [else
     "parsing error"]
  )
)

;; CONTRACT
;; interp : abstract-syntax -> number
;; take the info from parse, and interpret it so that it can be added.
(define (interp abstract)
  (cond
    [(structplus? abstract)
     (+ (structplus-left abstract)
     (structplus-right abstract))]
    [(structminus? abstract)
     (- (structminus-left abstract)
     (structminus-right abstract))]
    [(structmal? abstract)
     (* (structmal-left abstract)
     (structmal-right abstract))]
    [(structgeteilt? abstract)
     (/ (structgeteilt-left abstract)
     (structgeteilt-right abstract))]
    [else
     "interpreter error"]
   )
)
(check-expect (interp (parse program-one)) 8)
(check-expect (interp (parse program-two)) -1)
(check-expect (interp (parse program-three)) 6)
(check-expect (interp (parse program-four)) 2)

(test)
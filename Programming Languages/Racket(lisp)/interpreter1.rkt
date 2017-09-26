#lang racket
(require test-engine/racket-tests)

(struct DP (left right))

(define program-one '(DASPLUS 3 5))
(define program-two '(DASPLUS 0 -1))

(struct structplus (left right) #:transparent)

;; CONTRACT
;; parse : concrete-syntax -> abstract-syntax
;; take the info from program-one and change it's syntax
(define (parse concrete)
  (structplus (second concrete) (third concrete)))

;; CONTRACT
;; interp : abstract-syntax -> number
;; take the info from parse, and interpret it so that it can be added.
(define (interp abstract)
  (+ (structplus-left abstract)
     (structplus-right abstract)))

(check-expect (interp (parse program-one)) 8)
(check-expect (interp (parse program-two)) -1)

(test)
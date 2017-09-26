#lang racket
(require test-engine/racket-tests)

;; Environments -> stack
;; empty env
(define (empty-env) '())
;; tuple
(struct tuple (id value))
;; insert

(define (insert sym num ls)
   (cons (tuple sym num) ls)
)


(define (lookup x ls)
  (cond
    [(empty? ls) ls]
  (...)
)

  ;;Add environment to parse and interp (define (interp ast env)) and (interp (parse ...) (empty-env))


(check-expect (insert 'x 2 '()) '(x 2))

(test)
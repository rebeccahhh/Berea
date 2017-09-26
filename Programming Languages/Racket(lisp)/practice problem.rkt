#lang racket
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 3. Define a function that returnes the multiples of 2(any number really). Defined by the variable num
(define (what-the ls num)
  [cond
    [(empty? ls) 0]
    [(filter even? ls)]])

(check-expect (what-the '(1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16) 2) '(2 4 6 8 10 12 14 16))
(test)
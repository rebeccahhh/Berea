#lang racket
;; hours isa number
;; minutes isa number
(struct clock ([hours #:mutable] [minutes #:mutable]) #:transparent)

(define loc
  (list (clock 23 59)
        (clock 0 59)
        (clock 0 0)
        (clock 1 0)))




(define (tick clock)
  (cond
    [(equal?
      (remainder clock-minutes 59) 0) (set-clock-minutes! 0)
      (if (= (remainder clock-hours 23) 0)
      (set-clock-hours! 0) (set-clock-hours!
                            (+ clock-hours 1)))]
    [else
     (set-clock-minutes! (+ clock-minutes 1))]))
  



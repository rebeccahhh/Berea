#lang racket
;;Exercise 9.
;;Add the following line to the definitions area of DrRacket:
;;Then create an expression that converts whatever in represents to a number.
;;For a string, it determines how long the string is; for an image,
;;it uses the area; for a number, it decrements the number,
;;unless it is already 0 or negative; for #true it uses 10 and for #false 20.

(define in "hello")
(cond
  [(string? in)
    (string-length in)]
    )
(cond
  [(number? in)
    (print in)]
    )
(cond
  [(image? in)
   (do the area stuff)]
  )

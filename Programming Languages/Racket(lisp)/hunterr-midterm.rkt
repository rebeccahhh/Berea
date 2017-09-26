#lang racket
(require test-engine/racket-tests)

;; 1. contract!
;; generate-nums : num -> list
(define (generate-nums num)
  (cond
    [(zero? num) '()]
    [else
     (cons num (generate-nums (- num 1)))
    ]
  )
)

(check-expect(generate-nums 5) '(5 4 3 2 1))


;; 4. contract!
;; contains : number, value
;; generates : #t, #f
(define (contains ls val)
  (cond
    [(empty? ls) #f]
    [else
     (equal? val (first ls))
     (equal? val (contains (rest ls) val))
   ]
  )
)
(check-expect (contains '(1 2 3) 3) #t)
(check-expect (contains (generate-nums 5) 5) #t)
(check-expect (contains (generate-nums 5) 0) #f)

;; 4. contract!
;; contains : number, value
;; generates : #t, #f

(define (interesting? age)
  (cond
    [zero? (remainder age 3)]
    [zero? (remainder age 7)]
    [else #f]
  )
)
(check-expect (interesting? 3) #t)

;; 8. contract!
;; contains : list o'numbers
;; returns : smaller list o'numbers
(define (keep-interesting ls)
  [cond
    [(empty? ls) '()]
    [else
     [filter-not (interesting? (first ls)) ls]
     [filter-not (interesting? (keep-interesting (rest ls))) ls]
    ]
  ]
)
;;(check-expect (keep-interesting (generate-nums 8)) '(7 6 3))

;; 9. a freebie
(struct point (x y) #:transparent)
;; 10.
;; contains : a struct (and frustration)
;; generates : number
(define (manhattan point)
  (+ (abs (point-x point)) (abs (point-y point)))
)

(check-expect (manhattan (point 3 5)) 8)
(check-expect (manhattan (point -3 -5)) 8)

;; 11. 
(test)

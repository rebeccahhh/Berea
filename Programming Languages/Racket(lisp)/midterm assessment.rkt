#lang racket
(require test-engine/racket-tests)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
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

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4. contract!
;; contains : list, value
;; generates : #t, #f
(define (contains ls val)
  (cond
    [(empty? ls) #f]
    [(equal? val (first ls)) #t]
    [else
     (contains (rest ls) val)]
  )
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4. contract!
;; contains : number, value
;; generates : #t, #f

(define (interesting? age)
  (cond
    [(zero? (remainder age 3)) #t]
    [(zero? (remainder age 7)) #t]
    [else #f]
  )
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
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

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 9. a freebie
(struct point (x y) #:transparent)
;; 10.
;; contains : a struct (and frustration)
;; generates : number
(define (manhattan point)
  (+ (abs (point-x point)) (abs (point-y point)))
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; list and point/struct for use in number 11
(define list-of-points
  (list (point 8 1)
        (point 3 5)
        (point 0 9)
        (point 10 20)
   )
)
(define furthest-point (point 10 20))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 11. get-closest
;; contains : list, struct
;; returns : struct
(define (get-closest ls pt)
  (cond
    [(empty? ls) pt]
    [(< (manhattan (first ls)) (manhattan pt)) (first ls)]
    [else                                               
     (get-closest (rest ls) pt)
    ]
  )
)


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 12. interesting-points
;; contains : list -> list
(define (interesting-points ls)
  (cond
    [(empty? ls) 0]

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; the testing section
(check-expect(generate-nums 5) '(5 4 3 2 1))

(check-expect (contains '(1 2 3) 3) #t)
(check-expect (contains (generate-nums 5) 5) #t)
(check-expect (contains (generate-nums 5) 0) #f)

(check-expect (interesting? 3) #t)

;;(check-expect (keep-interesting (generate-nums 8)) '(7 6 3))

(check-expect (manhattan (point 3 5)) 8)
(check-expect (manhattan (point -3 -5)) 8)

(check-expect (get-closest list-of-points furthest-point)
              (point 3 5))
(test)

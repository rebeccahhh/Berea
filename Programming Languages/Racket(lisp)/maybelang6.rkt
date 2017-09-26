#lang racket
(require test-engine/racket-tests)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;; Structures ;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; some structures to aid in operations.
(struct structplus (left right) #:transparent)
(struct structminus (left right) #:transparent)
(struct structmal (left right) #:transparent) ;;multiply
(struct structgeteilt (left right) #:transparent) ;;divide
(struct structob (expression false true) #:transparent)
(struct structbinden (id bound-expression body) #:transparent)
(struct bound (id val) #:transparent)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; Parse ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; CONTRACT
;; parse : concrete-syntax -> abstract-syntax
;; take the info from program-# and change it's syntax
(define (parse concrete)
  (cond
    ;;check if it's already a number, if it is, return that
    [(number? concrete) concrete]
    ;;check if it's a symbol, if it is, return that
    [(symbol? concrete) concrete]
    ;;check if its addition, subtraction, multiplication, and division.
    [(equal? (first concrete) 'DASPLUS) (structplus (parse(second concrete)) (parse(third concrete)))]
    [(equal? (first concrete) 'DASMINUS) (structminus (parse (second concrete)) (parse(third concrete)))]
    [(equal? (first concrete) 'DASMAL) (structmal (parse(second concrete)) (parse(third concrete)))]
    [(equal? (first concrete) 'DASGETEILT) (structgeteilt (parse(second concrete)) (parse(third concrete)))]
    [(equal? (first concrete) 'ob0) (ob0 (parse(second concrete)) (parse(third concrete)) (parse(third (rest concrete))))]
    [(equal? (first concrete) 'DASBINDEN)
     (binden (first (second concrete)) (second (second concrete)) (rest(rest concrete))]
    ;;;dasbinden to go here
    [else
     (error 'parse "Error in ~a." (concrete))]
    )
  )
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;;;;;;;;;;;;;;;;;;;;;;;;;;;;; Interpret ;;;;;;;;;;;;;;;;;;;;;;;;;;;
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
    ;; if it's 0 or a bind it will *hopefully* return a number
    [else
     "interpreter error"]
    )
  )
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;




;;;;;;;;;;;;;;;;;;;;;;;;; Added Functions ;;;;;;;;;;;;;;;;;;;;;;;;;

;;CONTRACT
;; ob0 : number -> number        ;;ob is if in German...
;;check if the number is 0, return numeric versions of True and False
(define (ob0 expression true false) 
  (cond
    [(equal? 0 (interp expression)) false] ;; this will return 8, because it should.
    [else true]
    )
  )


;;ADD BINDEN AND SUB
;; symbol number -> 
(define (binden binder bindee expressions)
  (cond
    [(list? expressions) (binden binder bindee (rest expressions)) ]
    [
    (cond
      [(symbol? binder)
       (cond
         [(number? bindee) (bound binder bindee)]
         [else bindee]
         )
       ]
      [else (error "incorrect format for binden. ~a" binder)]
      )
    )

;; Ersatz = "substitute" auf deutsch
;; ersatz : ABSTRACT symbol expression -> ABSTRACT 
(define (ersatz abstract symbol expression)
  (cond
    [(number? abstract) abstract]
    ;; If it's a symobl, check for equality between abstract and symbol.
    [(symbol? abstract)
     (cond
       ;; return the expression if the abstract and symbol are the same
       [(equal? abstract symbol) expression]
       ;; else, do nothing
       [else abstract]
       )
     ]
    ;; if it's not a number or symbol, check to see if it's any of our structs
    ;; defined above. Call recursively on the contents of the structs.
    [(structplus? abstract)
     (structplus (ersatz (structplus-left abstract) symbol expression)
                 (ersatz (structplus-right abstract) symbol expression))]
    [(structminus? abstract)
     (structminus (ersatz (structminus-left abstract) symbol expression)
                  (ersatz (structminus-right abstract) symbol expression))]
    [(structmal? abstract)
     (structmal (ersatz (structmal-left abstract) symbol expression)
                (ersatz (structmal-right abstract) symbol expression))]
    [(structgeteilt? abstract)
     (structgeteilt (ersatz (structgeteilt-left abstract) symbol expression)
                    (ersatz (structgeteilt-right abstract) symbol expression))]
    [(structob? abstract)
     (structob (ersatz (structob-false abstract) symbol expression)
               (ersatz (structob-true abstract) symbol expression))]
    [(structbinden? abstract)
     (define inner-body       (structbinden-body abstract))
     (define inner-identifier (structbinden-id abstract))
     (define inner-bound-expression  (structbinden-bound-expression abstract)) 
     (ersatz (ersatz inner-body symbol expression)
             inner-identifier
             inner-bound-expression)]
    )
  )
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; Tests ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Programs to be tested!!!
(define eins '(DASPLUS 3 5))
(define zwei '(DASPLUS 0 -1))
(define drei '(DASMAL 2 3))
(define vier '(DASGETEILT 6 3))
(define fünf '(DASMINUS (DASMAL 2 3) 3))
(define sechs '(DASMINUS 5 3))
(define sieben '(DASMAL (DASMAL 2 1) (DASMAL 1 3)))
(define acht '(DASMINUS 5 3))
;;ob0
(define neun '{ob0 (DASPLUS 1 2) 8 -1} ) ;;changed because everything should always evaluate to 8
;;dasbinden 
(define zehn '{DASBINDEN {x 5} {DASPLUS x 3}})
(define elf '{DASBINDEN {x 5} {DASBIND {y 3} {DASPLUS x y}}})
(define zwölf '{DASBINDEN {x {DASPLUS 3 5}} {DASMINUS x 0}})

;;;;;;;;;;;;;;;;;;;;;;;;;;; Calling Tests ;;;;;;;;;;;;;;;;;;;;;;;;;;
(check-expect (interp (parse eins)) 8)
(check-expect (interp (parse drei)) 6)
(check-expect (interp (parse zwei)) -1)
(check-expect (interp (parse vier)) 2)
(check-expect (interp (parse fünf)) 3)
(check-expect (interp (parse sechs)) 2)
(check-expect (interp (parse sieben)) 6)
(check-expect (interp (parse acht)) 2)
(check-expect (parse neun) 8) ;;ob0
;; (check-expect (parse zehn) (bound 'x 5))
(check-expect (interp (parse elf)) 8)

(test)
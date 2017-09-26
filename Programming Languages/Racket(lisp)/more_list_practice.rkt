#lang racket
(require test-engine/racket-tests)
(define FIXME 'FIXME)

;; 1. Given a list of strings, write a function called keep-mandms.
;; Any string that begins with the letter 'm' will be kept, and
;; returned as part of a new list of strings.
(define (keep-mandms los) FIXME)

;; NOTE (20170214)
;; I forgot what happens when you grab the first element of a string!
;;  (string-ref "matt" 0)
;; will return the first character that is in the string "matt".
;; A character is a type, just like a boolean, number, and string.
;; (That means you can ask character? of things, and get a 
;; true/false answer.)
;; So, when you evaluate:
;;  (string-ref "matt" 0)
;; you get back
;; #\m
;; which is the character 'm', not a string of one character, which
;; would look like "m". So, for this problem, you'll need to ask
;; a question along the lines of
;;  (equal? (string-ref "matt" 0) #\m)
;; but, you might replace "matt" with a variable, or perhaps
;; the first string you find in a list of strings. 
;; Apologies for not realizing/remembering we had not seen
;; the character type before. This update is credited to 
;; an excellent question from one of your colleagues.

;; 2. Given a list of booleans, write a function called all-true?.
;; If every value in the list is true, then your function should
;; return true.
(define (all-true? lob) FIXME)

;; 3. Given a list of booleans, write a function called any-true?.
;; If any value in the list is true, you should return true.
(define (any-true? lob) FIXME)

;; A penguin isa
;; - height in cm (number)
;; - weight in kg (number)
;; - name (string)

;; 4. Given a list of penguins, write a function called total-weight.
;; This function should return their total weight in kg.
(define (total-weight lop) FIXME)

(define berea-penguins
  (list (penguin 19 5 "Mario")
        (penguin 21 6 "Scott")
        (penguin  6 2 "Simon")))

(check-expect (total-weight berea-penguins) 13)

;; 5. Given a list of penguins, write a function called get-shorties.
;; It should return a list of all of the penguins under 20cm tall.
(define (get-shorties lop) FIXME)

;; 6. Given a list of penguins, write a function called first-long-name.
;; It should return the first penguin it finds with a name longer
;; than 12 characters.
(define (first-long-name lop) FIXME)

;; 7. Challenge. Given a list of penguins, return the tallest penguin.
;; This function should be called get-tallest. Hint: You will need
;; to pass along the currently tallest penguin to solve this problem.
;; As a result, it looks a little different than previous problems.
;; So, it takes in a list of penguins and the (currently) tallest penguin,
;; and returns a penguin, which should be the tallest in the list.
(define (get-tallest lop tp) FIXME)

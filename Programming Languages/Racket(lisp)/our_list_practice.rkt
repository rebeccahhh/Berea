#lang racket
(require test-engine/racket-tests)

;; 1. Given a list of numbers, write a function called greater-than.
;; Keep any number greater than or equal to the number 7,
;; and return a new list of numbers.

;; 2. Write a function called separate-large that consumes a list of numbers and 
;; outputs a list of numbers that are greater than 12.

;; 3. Given a list of strings, write a function called longest-string that returns the 
;; string in the list with the largest number of characters.

;; 4. Given a list of numbers, return a list of all of the numbers that 
;; are a multiple of five.

;; 5. A question about ferrets (mustela putorius furo). First, define a
;; structure that represents a ferret.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;A ferret isa struct.
;; age: number
;; color: string
;; friendly?: boolean

;; Defining the struct should create the following functions
;;ferret : number string boolean-> ferret
;;ferret? : anything-> boolean
;;ferret-age : ferret-> number
;;ferret-color : ferret-> string
;;ferret-friendly? : ferret-> boolean

;; 6. Create a function called find-the-biters that takes in a list of ferrets
;; and returns a list of the ferrets that could potentially bite (ferrets that are not
;; friendly).

;; 7. First, define a structure that matches this contract.
#|
A cat isa
- color (string)
- tail? (boolean)
- name (string)
|#
;; 8. Given a list of cats, define a function called bobcats that
;;  returns a list of the names of all the cats with no tails.

;; 9. First, define a structure that matches the following contract.
#|
A student isa
name (string)
points-earned (number)
|#

;; 10. Given a list of students, define a function called favorite-student. 
;; This function should search through the list of students and return
;; the student who is obviously the professor's favorite.

;; 11. Given a list of numbers, find the average.
;; HINT: Write three functions. First, write a function called count-items.
;; This function should iterate through the list and find its length. The second
;; function, sum-items, should add up all the numbers in the list. Finally,
;; the third function, called average, should use these two functions to calculate
;; the average of all of the numbers in the list.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; song struct
; song-title -> string
; song-album -> string
; song-artist -> string

;; 12. Define a struct for songs.

(define list-of-songs
  (list (song "Migrane" "Vessel" "Twenty One Pilots")
        (song "Message Man" "Blurryface" "Twenty One Pilots")
        (song "Take Me to Church" "Hozier" "Hozier")
        (song "The Sound of Silence" "Disturbed" "Immortalized")
        (song "Pumped Up Kicks" "Foster the People" "Torches")
        (song "Sunrise" "Childish Gambino" "Camp")
        (song "Use Somebody" "Kings of Leon" "Only by the Night")
        (song "Goner" "Blurryface" "Twenty One Pilots")))

;; 13. Given a list of songs, write a function called 21-fans.
;; The function should return a list of songs by Twenty One Pilots.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; 14. Define a function say-it-i-dare-you that takes a list of numbers and 
; returns a list of strings that say "even" or "odd" for each number.

(check-expect (fun '(5 6 3 2 8) ) '("odd" "even" "odd" "even" "even"))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; A dog isa struct that contains
;; - name(string)
;; - breed (string)
;; - age (int)


;; 15. Define a struct for dogs.

;; 16. Given a list of dogs, define a function called old-dog, that returns
;; the oldest dog in the list.

;; 17. Define a function what-the that returns the multiples of a number of
;; the user's choice. 
(define (what-the lon mod))

(check-expect (what-the '(1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16) 2)
  '(2 4 6 8 10 12 14 16))
(check-expect (what-the '(1 3 5 7 9) 3) '(3 9))

;; 18. Write a function elim-by-pred that consumes a predicate 
;; (a function that returns boolean) and a list of numbers. 
;; It should produces the list of all numbers for which the given 
;; predicate returns false.
(define (three-or-seven? n)
  (or (equal? n 3) (equal? n 7)))

(check-expect (elim-by-pred three-or-seven? '(1 2 3 4 5)) '(3)))

;; 19. Write a function suffixes that consumes a list L (containing anything) 
;; and produces a list of all the suffixes of L. 
;; For example, (suffixes '(a b c d)) should produce ((a b c d) (b c d) (c d) (d) ()).

;; 20. Write a function called is-it-in-there? that takes a value and a list.
;; The function should return true if the value is in the list, and false otherwise.

(check-expect (is-it-in-there? 3 '(10 11 12)) #false)
(check-expect (is-it-in-there? "hello" '(1 2 "hello" 3)) #true)
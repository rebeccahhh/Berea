;; Rebeccah Hunter
;; My table consists of Nicholas Detore, Ashley Aiken, Hunter Wiseman, and Daryll Sullivan.
#lang racket
(require test-engine/racket-tests)
;; Matt got up early to write a quiz. He is sitting in the hotel restaurant, drinking coffee and eating breakfast while writing questions.
;; Assume coffee costs $1.38 per cup, eggs cost $0.83 each, and hash browns are $2.25 per serving.
;; Write a function called breaky-cost that returns his total cost for breakfast given the number of cups of coffee,
;; the number of eggs, and the number of orders of hash browns he eats.
(define (breaky-cost eg co hb)
  (+ (* co 1.38) (* eg 0.83) (* hb 2.25)))

(check-within (breaky-cost 3 2 1) 7.5 7.5)
(check-within (breaky-cost 4 3 2) 11.95 11.96)


;; Matt struggles with calculating tips. Write a function called calc-tip that, given a dollar amount and a percentage,
;; returns the amount he should leave as a tip. Because Matt is lazy, your percentage should be expressed as an integer;
;; eg. (calc-tip $2.76 20) to calculate a 20% tip on $2.76.
(define (calc-tip bill tip)
  (+ (* bill (/ tip 100)) bill))

(check-expect (calc-tip 10 20) 12)
(check-within (calc-tip 17.56 15) 20.194 20.194)


;; Matt was thinking of going for a walk this morning after writing the quiz. However, he's still not adapted to Maine temperatures.
;; Write a function called walking-in-lewiston? that consumes a temperature in  ̊F, and returns the strings "Yes!", "Maybe...", and
;; "Nopenopenope!" depending on whether the temperature is over 40˚, between 40 and 32˚ (inclusive), or below 32˚. 
(define (walking-in-lewiston temp)
  (cond
    [(< 40 temp) "Yes!"]
    [(and (>= 40 temp) (<= 32 temp)) "maybe..."]
    [(> 32 temp) "nopenopenopenope!"]))

(check-expect (walking-in-lewiston 45) "Yes!")
(check-expect (walking-in-lewiston 2) "nopenopenopenope!")


;; Matt goes for a walk, and realizes he can walk on the river, because it is frozen solid.
;; Unfortunately, it's sloped. Implement the acceleration formula (vfinal = vinitial + (acceleration*time)) in a function called calc-accel.
;; Assuming Matt begins walking down the slope of the river at 1m/second, looses his footing on the wet ice, and begins to
;; slide down the practically frictionless ice under an acceleration of 9.8m/s2, how fast will be he going when he gets to
;; the bottom of the slope 8 seconds later?
(define (calc-accel seconds)
  (+ 1 (* 9.8 seconds)))

(check-within (calc-accel 8) 79.4 79.4)
(check-within (calc-accel 2) 20.6 20.6)


;; Does Matt go splat when he hits a tree? It turns out that the terminal velocity of a skydiver is 53 m/s,
;; which (if they don't pull their parachute) is a Very Bad Speed for coming to rest on the planet Earth.
;; Implement goes-splat? such that it consumes the number of seconds that Matt slides down the ice, and returns #true if
;; he will go splat when he hits the tree (if he is traveling at greater than terminal velocity), and #false if he is moving slower.
(define (goes-splat? seconds)
  (cond
    [(>= (calc-accel seconds) 53) #t]
    [(< (calc-accel seconds) 53) #f]))

(check-expect (goes-splat? 7) #t)
(check-expect (goes-splat? 1) #f)
(check-expect (goes-splat? 0) #f)
;; I'm very concerned it appears that regardless of how little time you fall,
;; you will go splat... I've checked my math.. but maybe it's wrong?



;; Matt comes back to the hotel after experimenting with physics on the rivers of Lewiston/Auburn.
;; The song Call Me Maybe by Carly Rae Jepsen comes on the hotel speakers. Write a function called
;; oh-noes that consumes the number of times Matt hears the song in his head through the rest of the day,
;; and returns the number of seconds he "listens" to the song. For example, Call Me is 3m13s long; if he invokes (oh-noes 2), it would return 386.
(define (oh-noes plays)
  (* 193 plays))

(check-expect (oh-noes 7) 1351)
(check-within (oh-noes 3.2) 617.6 617.6)

;; Matt realizes he is 1200 miles from Berea, Kentucky. There are 5280 feet in a mile. Matt's office is 1500 feet from his front door.
;; Write a function called walks-to-la that consumes the number of times Matt walks to or from his office,
;; and returns how many more times he would have to do that walk before he walked the rest of the way to Lewiston, Maine.
;; For example, if Matt walks back-and-forth to his office 2 times in a day (4 trips of 1500'), he would have to do it 4,220 more times to reach Maine.
(define (walks-to-la walks)
  (/ (-  6336000 (* walks 1500)) 1500))

(check-expect (walks-to-la 4) 4220)
(check-expect (walks-to-la 64) 4160)

;; Matt is getting email asking him questions. He's tired of writing the same thing over-and-over. So, he writes a Racket program to answer his email.
;; Implement generic-answer as a function that consumes a name as a string, and returns a string with a polite message like
;; "Dear <name>, I'm not here. Please stop writing me." The name given should be inserted in the indicated place in the string.
(define (generic-answer name)
  (string-append "Dear " name ", I'm not here. Please stop writing me"))

(check-expect (generic-answer "Ronald") "Dear Ronald, I'm not here. Please stop writing me")
(check-expect (generic-answer "Nick") "Dear Nick, I'm not here. Please stop writing me")


;; Matt realizes his boss might get the above message, and that could go over poorly. Write a new function called safe-answer that
;; consumes a name and, if it is "Chad", "Mario", or "Nancy", it returns "Hi <name>, I'll get back to you as soon as possible!"
;; However, if it is anyone else, then the function safe-answer should just call generic-answer.
(define (safe-answer name)
  (if (or (string=? name "Chad") (string=? name "Mario") (string=? name "Nancy")) (string-append "Hi " name ", I'll get back to you as soon as possible!")
     (string-append "Dear " name ", I'm not here. Please stop writing me")))

(check-expect (safe-answer "Ronald") "Dear Ronald, I'm not here. Please stop writing me")
(check-expect (safe-answer "Chad") "Hi Chad, I'll get back to you as soon as possible!")


;; Matt was tempted to only have 9 questions. Instead, he decided on one more, mind-bending question. Implement a function called awesome!
;; that consumes no arguments, and it returns the string "AWESOME!"
(define awesome "AWESOME!")
(define awesome? "AWESOME!!!")

(test)

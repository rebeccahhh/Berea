; Load the number 3 into the A register
@3
; Move the number 3 into the D register
D=A

; Load the number 5 into the A register
@5

; Store the sum of D an A into the D register
D=D+A

; Load 12 into the A register.
; This is because I want to store to 
; this address in RAM 
; with the following instruction
@12

; Store the D register into RAM.
; We will store the value of the D register
; into RAM at the address that is currently
; contained in the A register.
M=D



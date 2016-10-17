// Load 3 into the AReg
@3
// Set DReg equal to the AReg
D=A
// Load 5 into the AReg
@5
// Set D equal to the sum of D+A
D=D+A
// Load a RAM address into AReg
@0
// Store the DReg into RAM[0]
M=D
; // Go back to the begining
; //@0
; // no jump
; //0;JMP


#include "bitshifting.h"


/* FUNCTION shift_left : int16 int -> int16
      PURPOSE: Shift the bits of a given sixteen bit integer left
      a given number of places, returning the 16-bit result.*/
int16 shift_left (int16 number, int places) {
  int shifted = number << places;
  return shifted;
}

/* FUNCTION shift_right : int16 int -> int16
      PURPOSE: Shift the bits of a given sixteen bit integer right
      a given number of places, returning the 16-bit result.*/
int16 shift_right (int16 number, int places) {
  int shifted = number >> places;
  return shifted;  
}

/* FUNCTION apply_mask : int16 int16 -> int16
      PURPOSE: Given a number and a mask, apply that mask. The resulting number
      should preserve values anywhere that the mask has 1s.*/
int16 apply_mask (int16 number, int16 mask) {
  /* Your code should go here, and return the correct thing. */
  int intermediate = number & mask;
  int final = intermediate | mask;
  return final;  
}

/* FUNCTION set_one_bit : int16 int -> int16
      PURPOSE: Given a bit position (a number between 0 and 15), 
      that bit in a given number should be set to 1.*/
int16 set_one_bit (int16 number, int bit_position) {
  /* Your code should go here, and return the correct thing. */
  int new = 1;
  int final = shift_left(new, bit_position);
  int fin = number | final;
  return fin; 
}

/* FUNCTION clear_one_bit : int16 int -> int16
      Purpose: Given a bit position (a number between 0 and 15).
      that bit in a given number should be set to 0.*/
int16 clear_one_bit (int16 number, int bit_position) {
  /* clears one bit in a given bit position. */
  int new = 1;
  int final = shift_left(new, bit_position);
  int fin = number ^ final;
  return fin; 

}

/* FUNCTION set_multiple_bits : int16 int16 -> int16
      Purpose: Given a mask of bits, those bits in a target number
      should all be set to 1. Anywhere the mask is 0, those 
      values should remain unchanged in the original number.*/
int16 set_multiple_bits (int16 number, int16 mask) {
  /* Your code should go here, and return the correct thing. */
  int final = number | mask;
  //int final = intermediate | number;
  return final; 
}

#include "decode.h"

/* get_i_bit:
 * MASKS out the i bit from the instruction, shifts it 
 * to the LSB position, and returns that value.
 */
int16 get_i_bit (int16 instr) {
//   int shifted = instr >> 15;
//   return shifted;

//  NEW INSTRUCTIONS:
  // Mask: 1000 0000 0000 0000
  // Shift the MSB to tLSB
  int16 mask = 0x8000;
  int16 masked = apply_mask(instr, mask); 
  int16 out = shift_right(masked, 15);
  //printf("iget_i_bit: %04x \n", out); 
  //The 0 means "pad with zeros", the 4 means "at least four characters wide".
  return out; 
}

/* get_a_bit:
 * MASKS out the a bit from the instruction, shifts it 
 * to the LSB position, and returns that value.
 */
int16 get_a_bit (int16 instr) {
//   int shift_one = instr << 3;
//   int shifted = shift_one >> 15;
//   return shifted;

//  NEW INSTRUCTIONS:
  // Mask: 0001000000000000
  // Or, this might be wrong. You fix it. - thanks...?
  int16 mask = 0x1000;
  int16 masked = apply_mask(instr, mask);
  int16 shifted = shift_right(masked, 12);
  return shifted;
}

/* get_c_bits:
 * MASKS out the c bits from the instruction, shifts them 
 * to the LSB position, and returns that value.
 */
int16 get_c_bits (int16 instr) {
//   int shift_one = instr << 4;
//   int shifted = shift_one >> 10;
//   return shifted;

//  NEW INSTRUCTIONS:
  // mask: 0000 1111 1100 0000
  int16 mask = 0xFC0;
  int16 masked = apply_mask(instr, mask);
  int16 out = shift_right(masked, 6);
  return out;
  
}

/* get_d_bits:
 * MASKS out the d bits from the instruction, shifts them 
 * to the LSB position, and returns that value.
 */
int16 get_d_bits (int16 instr) {
//   int shift_one = instr << 10;
//   int shifted = shift_one >> 13;
//   return shifted;

//  NEW INSTRUCTIONS:
  // mask: 0000 0000 0011 1000
  int16 mask = 0x0038;
  int16 masked = apply_mask(instr, mask);
  int16 out = shift_right(masked, 3);
  return out;
}

/* get_j_bits:
 * Masks out the j bits from the instruction, shifts them 
 * to the LSB position, and returns that value.
 */
int16 get_j_bits (int16 instr) {
//   int shift_one = instr << 13;
//   int shifted = shift_one >> 13;
//   return shifted;

// NEW INSTRUCTIONS
  //mask: 0000 0000 0000 0111
  int16 mask = 0x07;
  int16 masked = apply_mask(instr, mask);
  return masked;
}

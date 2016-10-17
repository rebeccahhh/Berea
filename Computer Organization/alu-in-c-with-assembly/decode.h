#ifndef DECODE_H
#define DECODE_H
#include "hacktypes.h"

int16 get_i_bit (int16 instr);
int16 get_a_bit (int16 instr);
int16 get_c_bits (int16 instr);
int16 get_d_bits (int16 instr);
int16 get_j_bits (int16 instr);

#endif /* DECODE_H */

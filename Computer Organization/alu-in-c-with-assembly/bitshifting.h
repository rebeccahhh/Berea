// #ifndef BITSHIFTING_H
// #define BITSHIFTING_H
#include "hacktypes.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// typedef int16_t int16;
typedef int8_t byte;

int16 shift_left (int16 number, int places);

int16 shift_right (int16 number, int places);

int16 apply_mask (int16 number, int16 mask);

int16 set_one_bit (int16 number, int bit_position);

int16 clear_one_bit (int16 number, int bit_position);

int16 set_multiple_bits (int16 number, int16 mask);


//#endif
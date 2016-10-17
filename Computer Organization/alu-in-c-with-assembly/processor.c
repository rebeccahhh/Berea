/* Includes */
#include <stdio.h>
#include "processor.h"
#include "allyourbase.h"

/* Functions */

void show_alu_flags (int16 flags) {
  printf("Flags: ");
  base2(flags);
}

/* get_bit
 * PURPOSE:
 * Extract a single bit from a value. We will extract
 * the bit given by the parameters "bitnumber".
 * For example, given the value
 * 0b00100
 * and the bitnumber 2, we should get back a 1.
 * (The bitnumber is zero-indexed.)
 *
 * This function should be handy in the ALU below...
 */
int get_bit (int16 value, int bitnumber) {
  int16 mask = shift_left(1, bitnumber);
  int16 masked = apply_mask(value, mask);
  int16 final = shift_right(masked, bitnumber);
  return final;
}

/* alu
 * PARAMETERS: x, y, bool* flags, bool *ng, bool *zr
 * PURPOSE:
 * Runs calculations as described in EoCS.
 */
int alu (int x, int y, int16 flags, bool *ng, bool *zr)
{
  /* Your ALU goes here. 
   * Your ALU will need to be modified slightly.
   * instead of using an array, you now need to extract
   * the correct bit for each flag.
   * Don't forget to set ng and zr.
   */
  
  // I owe this entire section to Ashley, she is so helpful
  // in every way, and also so nice! She was amazing and helped
  // me out so much.
   int16 zx = get_bit(flags, 5);
   int16 nx = get_bit(flags, 4);
   int16 zy = get_bit(flags, 3);
   int16 ny = get_bit(flags, 2);
   int16 f = get_bit(flags, 1);
   int16 no = get_bit(flags, 0);

   
   
  // show_alu_flags(cbits);
    int out; //declare int variable out
    
    if (zx == 1){ //if zx is true
      x = 0; //x is zero
    }
    if (nx == 1){ // if nx is true
      x = ~x; //x is not x (I couldn't get the ~ to work)
    }
    if (zy == 1){ // if zy is true
      y = 0; // y is zero
    }
    if (ny == 1){ // if ny is true 
      y = ~y; //y is not y (i couldn't get the ~ to work)
    }
    if (f == 1){ // if f is true 
      out = x + y; // out is x plus y
    }
    else { // else 
      out = x & y; // out is x and y
    }
    
    if (no == 1){ // if no is true 
      out = ~out; // out is not out (couldn't get ~ to work)
    }
    if (out < 0){
      *ng = true;
      //printf("Ng: %d", ng);
    }
    else{
      *ng = false;
     // printf("Ng: %d", ng);
    }
    if(out == 0){
      *zr = true;
      //printf("Zr: %d", zr);
    }
    else{
      *zr = false;
      //printf("Zr: %d", zr);
    }
    //printf("%i\n", out);
    return out; // return out. 
  
  return 0;
}
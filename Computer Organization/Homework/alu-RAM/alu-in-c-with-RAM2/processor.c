/* Includes */
#include <stdio.h>
#include "processor.h"

/* Functions */

void show_alu_flags (bool *flags) {
  int ndx;
  for (ndx = 0 ; ndx < NUM_ALU_FLAGS; ndx++) {
    if (flags[ndx]) {
      printf ("Flag %i: True\n", ndx);
    } else {
      printf ("Flag %i: False\n", ndx);
    }
  }
}

/* set_flags
 * PARAMETERS: bool *flags, bool zx, nx, zy, ny, f, no
 * PURPOSE:
 * Takes six boolean values, and stores them into the array
 * pointed at by the *flags pointer. Makes it easier to 
 * set up the flags 'array', because you can repeatedly call
 * this function and quickly set all six locations.
 * Typically used before calling the alu() function.
 */
void set_flags(bool *flags, bool zx, bool nx, bool zy, bool ny, bool f, bool no){
  flags[0] = zx;
  flags[1] = nx;
  flags[2] = zy;
  flags[3] = ny;
  flags[4] = f;
  flags[5] = no;
  
}



/* alu
 * PARAMETERS: x, y, bool* flags, bool *ng, bool *zr
 * PURPOSE:
 * Runs calculations as described in EoCS.
 */
int alu (int x, int y, bool *flags, bool *ng, bool *zr)
{
  /* Your ALU goes here. */
  /* Update it to set ng and zr. */
    show_alu_flags(flags);
    int out; //declare int variable out
    if (flags[0] == true){ //if zx is true
      x = 0; //x is zero
    }
    if (flags[1] == true){ // if nx is true
      x = ~x; //x is not x (I couldn't get the ~ to work)
    }
    if (flags[2] == true){ // if zy is true
      y = 0; // y is zero
    }
    if (flags[3] == true){ // if ny is true 
      y = ~y; //y is not y (i couldn;t get the ~ to work)
    }
    if (flags[4] == true){ // if f is true 
      out = x + y; // out is x plus y
    }
    else{ // else 
      out = x & y; // out is x and y
    }
    if (flags[5] == true){ // if no is true 
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
}
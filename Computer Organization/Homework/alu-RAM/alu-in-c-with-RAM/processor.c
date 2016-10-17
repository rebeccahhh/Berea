/* Includes */
#include <stdio.h>
#include "processor.h"

/* Functions */

void show_alu_flags (bool *flags) {
  for (int ndx = 0 ; ndx < NUM_ALU_FLAGS; ndx++) {
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



/* alu
 * PARAMETERS: x, y, bool* flags, bool *ng, bool *zr
 * PURPOSE:
 * Runs calculations as described in EoCS.
 */
int alu (int x, int y, bool *flags, bool *ng, bool *zr) {
  /* Call show_alu_flags with the correct parameter. */
    show_alu_flags(flags);
    int out;
    if (flags[0] == true){ /*if zx is true*/
      x = 0; /*x = zero*/
    }
    if (flags[1] == true){ /* if nx is true*/
      x = ~x; /*out = not x */
    }
    if (flags[2] == true){ /* if zy is true*/
      y = 0; // y is zero
    }
    if (flags[3] == true){ /* if ny is true*/ 
      y = ~y; /*out = not y */ 
    }
    if (flags[4] == true){ // if f is true 
      out = x + y; /* out = x+y*/
    }
    else{ /* else*/ 
      out = x & y; /* out = x and y*/ 
    }
    if (flags[5] == true){ /* if no is true */ 
      out = ~out; /* = not out*/ 
    }
    if (out = 0){
      *zr = true;
      printf("ZR: %i", &zr);
    }
    if (out < 0){
      *ng = true;
      printf("NG: true");
    }
    //printf("%i\n", out);
    return *zr;
    return *ng;
    return out; // return out. 

  
  return x + y; 
}
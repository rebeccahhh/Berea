/* Includes */
#include <stdio.h>
#include "processor.h"
#include <stdbool.h>

/* Functions */

void show_alu_flags (bool *flags) {
  /* Insert code here to print the true/false value of each flag. */
  int check;
  int total = ALU_FLAGS;
  for (check = 0; check < total; check++){
      printf("|%d|\n", flags[check]);
  }
}


int alu (int x, int y, bool *flags, bool *zr, bool *ng) {
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

  /* Do the calculations of the ALU here. */
}
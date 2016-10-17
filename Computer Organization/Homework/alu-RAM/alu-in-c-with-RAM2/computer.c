/*This ALU in C would NOT have been possible without Ashley Aiken. She helped me *
 *out immensely and took time to work with me individually while she was working *
 *on her own ALU so that I could work with her to understand. Also her Ferrets   *
 *were extremely helpful as well. I highly reccomend them as personal assistants.*/


// Includes
#include <stdio.h>
#include <stdlib.h>
#include "processor.h"
#include "ram.h"
int RAM[RAMSIZE];

// Main 
int main () {
  /* Variable declarations. 
   * You may declare others, but these were all I needed. 
   */
  bool *flags, *ng, *zr;
  int result, ndx, x, y;
  printf("Enter x: "); //I have the user enter x
  scanf("%i", &x);
  //printf("%i", x);
  printf("Enter y: "); //Enter y
  scanf("%i", &y);
  //printf("%i", y)
  /* Allocate space for the flags. */
  flags =(bool*)malloc(NUM_ALU_FLAGS);
  /* Allocate space for NG and ZR */
  ng = (bool*)malloc(1);
  zr = (bool*)malloc(1);
  
  /* Zero RAM. */
  init_ram();
  
  /* Begin by storing 1 at location 0 in RAM, and 1 at location 1. */
  set_ram(0, 1);
  set_ram(1, 1);
  
  /* Set the flags. Use your new set_flags function. */
  set_flags(flags, false, false, false, false, false, false);
  //alu_result = alu(x, y, flags);
  //printf ("Result: %i\n", alu_result);

  /* Add locations zero and one in ram. */
  int addition = get_ram(0) + get_ram(1);
  
  /* Store the result of your previous computation
   * at location 2 in RAM. */
   set_ram(2, addition);
  
  /* Show the first 8 slots in RAM */
  show_ram(0, 8);

  /* Print a pretty divider. */
  printf("==================\n");
  
  /* Zero memory. */
  init_ram();

  /* Store 1s at locations 0 and 1. */
  set_ram(0, 1);
  set_ram(1,1);
  

  /* Iterate:
   * Add location 0 and 1, storing in 2.
   * Add location 1 and 2, storing in 3.
   * Add location 2 and 3, storing in 4.
   * Add location 3 and 4, storing in 5...
   * Repeat through location 16.
   * What numerical sequence have you implemented? 
   
   The fibonacci sequence?
   */
   for(ndx = 0; ndx < 15; ndx++) {
     int temp = get_ram(ndx) + get_ram(ndx+1);
     set_ram(ndx+2, temp);
     //printf("RAMndx: %i\nRAMndx+1: %i\nRAMndx+2: %i\n", RAM[ndx], RAM[ndx+1], RAM[ndx+2]);
   }
  
   /* Show the RAM from 0 to 16. */
   show_ram(0, 16);

  /* End of main. Return a value that indicates
   * that no errors have occurred.
   */ 
  return 0;
}
/* Includes */
#include <stdio.h>
#include "processor.h"
#include "processor.c"
#include <stdbool.h>

/* Main */
int main () {
  /* Variable declarations */
  bool flags[ALU_FLAGS] = {false,true,false,true,false,true};
  bool *zr;
  bool *ng;
  int alu_result;
  int x, y;
  /* Read in values */
  /* Read in values from the user for x and y. */
  printf("Enter x: "); //I have the user enter x
  scanf("%i", &x);
  //printf("%i", x);
  printf("Enter y: "); //Enter y
  scanf("%i", &y);
  //printf("%i", y);
  /* Set Flags */
  /* Read in values from the user for the six boolean flags
  * that the ALU requires (zr, nz, etc.).
  */
  /* Do computations */
  alu_result = alu(x, y, flags, zr, ng);

  /* Print result */
  printf ("Result: %i\n", alu_result);

  /* End of main. Return a value that indicates
   * that no errors have occurred.
   */
  return 0;
}
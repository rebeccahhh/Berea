#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/* Constants */
#define NUMBER_OF_TESTS 4
#define A 0
#define B 1

void And (bool a, bool b, bool *out) {
  if (a && b) {
    *out = true;
  } else {
    *out = false;
  }
} 

void Xor (bool a, bool b, bool *out) {
  if (a ^ b){
    *out = true;
  }
  else{
    *out = false;
  }
}

void HalfAdder (bool a, bool b, bool* sum, bool* carry) {
  Xor(a, b, sum);
  And(a, b, carry);
}

int main () {
  bool a, b;
  bool *r1, *r2;
  bool tests[4][2] = {{false, false}, 
                      {false, true}, 
                      {true, false},
                      {true, true}
                    };
  int ndx;
  
  /* Allocate space for pointers */
  r1 = (bool *)malloc(sizeof(bool));
  r2 = (bool *)malloc(sizeof(bool));

  /* Test And */
  for (ndx = 0; ndx < NUMBER_OF_TESTS ; ndx++) {
    And (tests[ndx][A], tests[ndx][B], r1);
    printf("And: %i %i -> %i\n",
           tests[ndx][A], 
           tests[ndx][B],
           *r1
          );
  }  
  
  /* Print a pretty separator */
  printf("-=-=-=-=-=-=-=-=-=-=-=--=-=\n");
  
  /* Test Xor */
  for (ndx = 0; ndx < NUMBER_OF_TESTS ; ndx++) {
    Xor (tests[ndx][A], tests[ndx][B], r1);
    printf("Xor: %i %i -> %i\n",
           tests[ndx][A], 
           tests[ndx][B],
           *r1
          );
  }
  
  /* Print a pretty separator */
  printf("-=-=-=-=-=-=-=-=-=-=-=--=-=\n");
  
  /* Test HalfAdder */
  for (ndx = 0; ndx < NUMBER_OF_TESTS ; ndx++) {
    HalfAdder(tests[ndx][A],tests[ndx][B], r1, r2);
    printf("HalfAdder: %i %i -> %i %i\n",
           tests[ndx][A], 
           tests[ndx][B],
           *r1,
           *r2
          );
  }
  printf("-=-=-=-WooooWooooo!!!!!-=-=-=\n");
  return 0;
}
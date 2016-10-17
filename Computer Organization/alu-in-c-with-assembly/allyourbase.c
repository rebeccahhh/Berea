#include "allyourbase.h"

const char *bit_rep[16] = {
    [ 0] = "0000", [ 1] = "0001", [ 2] = "0010", [ 3] = "0011",
    [ 4] = "0100", [ 5] = "0101", [ 6] = "0110", [ 7] = "0111",
    [ 8] = "1000", [ 9] = "1001", [10] = "1010", [11] = "1011",
    [12] = "1100", [13] = "1101", [14] = "1110", [15] = "1111",
};

void base2 (int16 n) {
  byte MSB, LSB;
  
  // Why does this give me what I want?
  MSB = n >> 4;
  LSB = n & 0x0F;
  
  printf ("0b%s%s", bit_rep[MSB],  bit_rep[LSB]);
}


void base16 (int16 n) {
  printf("0x%02X", n);
}


// MCJ 20151103
// I wrote this function because I hate having to write "\n".
void newline () {
  printf("\n");
} 

// This function formats numbers nicely, so you
// can see both the binary and hex.
void b2b16 (int16 n) {
  base2(n);
  printf( " [ ");
  base16(n);
  printf( " ]");
  newline();
}

// This function just prints a message followed by the word "passed."
void passed (char *msg) {
  printf("%s passed.", msg);
  newline();
}

// This function nicely formats the output when a test fails.
void failed (char *msg, int16 expected, int16 received) {
  printf("%s FAILED.", msg);
  newline();
  printf("\texpected: ");
  b2b16(expected);
  newline();
  printf("\treceived: ");
  b2b16(received);
  newline();
}

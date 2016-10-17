#ifndef ALLYOURBASE
#define ALLYOURBASE

#include <string.h>
// For int16 type.
#include "bitshifting.h"

void base2 (int16 number);
void base16 (int16 number);

void newline ();
void b2b16 (int16 n);
void passed (char *msg);
void failed (char *msg, int16 expected, int16 received);

#endif /* ALLYOURBASE ARE BELONG TO US */
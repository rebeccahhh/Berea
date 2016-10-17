#ifndef RAM_H
#define RAM_H
#include "hacktypes.h"

/* Define the size of our RAM in words */
#define RAMSIZE 512

/* Functions for operating on RAM. */
void init_ram ();
void set_ram (int16 location, int16 value);
int16  get_ram (int16 location);
void show_ram (int16 start, int16 end);

#endif /* RAM_H */
#ifndef RAM_H
#define RAM_H

/* Define the size of our RAM in words */
#define RAMSIZE 512

/* Functions for operating on RAM. */
void init_ram ();
void set_ram (int location, int value);
int  get_ram (int location);
void show_ram (int start, int end);

#endif /* RAM_H */
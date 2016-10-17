#include "ram.h"
#include "errors.h"
#include "stdio.h"
/* Our RAM array. 
 * It is global to this file.
 */
int RAM[RAMSIZE];

/* init_ram
 * PARAMETERS: none
 * PURPOSE:
 * Iterates through the entire RAM array, storing zeroes
 * at each location.
 */
void init_ram() 
{
  int check;
  int total = RAMSIZE;
  for (check = 0; check < total; check++)
    {RAM[check] = 0;}
}

/* set_ram
 * PARAMETERS: int location, int value
 * PURPOSE:
 * Takes in a location and value. Makes sure that you are writing
 * to a valid RAM location, and stores the value at that location.
 * Otherwise, exits with ERR_SEGFAULT.
 */
void set_ram (int location, int value) 
{
    if (location > RAMSIZE)
        {ERR_SEGFAULT;}
    
    else if (location < 0 )
        {ERR_SEGFAULT;}
    
    else 
        {RAM[location] = value;}
}

/* get_ram
 * PARAMETERS: int location
 * PURPOSE:
 * Returns a value from a RAM location.
 */
int get_ram (int location) 
  {
    return RAM[location];
  
  }

/* show_ram
 * PARAMETERS: int, int
 * PURPOSE:
 * Prints the values of RAM from the start to end location.
 */
void show_ram (int start, int end) 
  {
    int variable;
    for (start; start < end; start++)
      {
        variable= RAM[start];
        printf("|%i|\n", variable);
      }
  }
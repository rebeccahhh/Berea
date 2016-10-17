/* See this Stack Overflow:
 * http://stackoverflow.com/questions/1653958/why-are-ifndef-and-define-used-in-c-header-files
 * And also google "include guards in c" for more information.
 */
#ifndef PROCESSOR_H
#define PROCESSOR_H

/* Includes */
/* See 
 * http://stackoverflow.com/questions/1921539/using-boolean-values-in-c
 * Regarding booleans in C.
 */
#include <stdbool.h>
#include "hacktypes.h"

/* Function Declarations */
int alu (int x, int y, int16 flags, bool *ng, bool *zr);

#endif

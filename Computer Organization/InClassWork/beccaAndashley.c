/* Things to do:
 * Two pointers:
   - middle, finger

 * An array.
   - upupandarray

 * A function that took the pointer
   and printed both the address
   of the pointer and the value
   located at that address.

   - just_do_it

 * A function that takes a pointer
   as an argument, and modifies
   the value at the given address.

    - shia_surprise

 * A function that takes an array
   and the length of the array,
   and prints all of the values
   in that array.

    - actual_cannibal
 */
#include <stdio.h>
void just_do_it (int upupandarray[], int location){
    /*A function that took the pointer
   and printed both the address
   of the pointer and the value
   located at that address.*/
   int *pointer = &upupandarray[location];
   printf("%p\n", pointer);
   printf("value = |%d|\n", upupandarray[location]);
}


int main(){
    int upupandarray[5] = {80,15,23,32,47};
    just_do_it(upupandarray, 2);
    return 0;
}

void show_me(int *thing){
    //void is used when nothing is returned in a function
    //Cody is a loch ness monster
}

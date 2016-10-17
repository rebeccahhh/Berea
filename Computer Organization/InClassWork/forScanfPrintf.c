/*
* Obligatory Comment
*/
# include <stdio.h>
int main()
{
    int x = 1;
    for ( x = 1; x<10; x++ ) {
        printf("I am %i years old\n", x);
        scanf("%i", &x); /*resets x to the users input*/
    }
    return 0;
}
/* 
Writing outside the bounds of a block of allocated memory can corrupt data, crash the program, or cause the execution of malicious code. C++ is particularly vulnerable to buffer overflows.

modified from http://cis1.towson.edu/~cssecinj/modules/cs0/buffer-overflow-cs0-c/
*/

#include <iostream>; //for keyboard input and screen output
using namespace std; // needed to simplify standard libraries

int main ()
{
    int buffer[5]; 
    int importantData = 100;
    for (int i=0; i<=6; i++){
	    buffer[i]=7;
	    cout << i <<" ";
    }
    cout << "after buffer overfow: " << endl;
    cout << importantData << endl;

    return 0; //this is typical of the last line of a C++ program
}

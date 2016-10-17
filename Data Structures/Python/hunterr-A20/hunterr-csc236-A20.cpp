#include <fstream>  // this is to import the ifstream and ofstream objects
#include <iostream>  // this is to import the cin and cout objects
#include <stack>
using namespace std;

// precondition: theFile refers to a stream that has been opened already
// postcondition: the contents of the file have been read and output to the console
void read_file( ifstream& theFile ) {
    string buffer;  // this string will read in the buffer from the file 
    stack<string> mystack;
    // while there are still things in the file to read in, read it in and output to console.
    while( theFile.eof() == false ) {
        theFile >> buffer;
        mystack.push(buffer);
        //cout << buffer << endl; // print the string and a newline 
    }
    
    while( !mystack.empty() ) {
        cout << mystack.top() << endl;
        mystack.pop();
    }
}

int
main() {
    ifstream theInputFile;
    theInputFile.open("input.txt"); // Open the file with the name "inputFile.txt". 

    // pass the file stream into the read_file() function. 
    read_file( theInputFile );
    theInputFile.close();
    return 0;
}
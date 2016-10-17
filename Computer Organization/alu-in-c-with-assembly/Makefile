# http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/
CC=gcc
CFLAGS=-std=gnu99 -I. 

%.o: %.c
	$(CC) -c -o $@ $< $(CFLAGS)

hackcpu: ram.o processor.o decode.o bitshifting.o allyourbase.o computer.o
	gcc -o hackcpu ram.o processor.o decode.o bitshifting.o allyourbase.o computer.o -I.

clean:
	rm -f *.o
	rm -f hackcpu
	
all: clean hackcpu
	echo "Done."

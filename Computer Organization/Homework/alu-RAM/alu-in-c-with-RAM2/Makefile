# http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/
CC=gcc
CFLAGS=-std=gnu99 -I. 

%.o: %.c
	$(CC) -c -o $@ $< $(CFLAGS)

hackcpu: ram.o processor.o computer.o
	gcc -o hackcpu ram.o processor.o computer.o -I.

all: hackcpu
	echo "Done."

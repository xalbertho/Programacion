prog=main.exe

all: $(prog)
	./$(prog)

$(prog): main.c recursion.h recursion.o
	gcc main.c recursion.o -o $(prog)

recursion.o: recursion.c
	gcc -c recursion.c -o recursion.o
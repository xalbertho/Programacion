run: main.exe
	./main.exe

main.exe: main.c operaciones.h tools.h operaciones.o tools.o
	gcc main.c operaciones.o tools.o -o main.exe

operaciones.o: operaciones.c
	gcc -c operaciones.c -o operaciones.o

tools.o: tools.c
	gcc -c tools.c -o tools.o

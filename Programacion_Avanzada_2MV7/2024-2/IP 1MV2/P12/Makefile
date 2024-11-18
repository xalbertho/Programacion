run: main.exe
	./main.exe

main.exe: main.c funciones.h funciones.o
	gcc main.c funciones.o -o main.exe

funciones.o: funciones.c
	gcc -c funciones.c -o funciones.o
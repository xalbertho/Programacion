prog=prog.exe

run: $(prog)
	./$(prog)

$(prog): main.c funciones/cadena.h funciones/cadena.o
	gcc main.c funciones/cadena.o -o $(prog)

cadena.o: funciones/cadena.c
	gcc -c funciones/cadena.c -o cadena.o
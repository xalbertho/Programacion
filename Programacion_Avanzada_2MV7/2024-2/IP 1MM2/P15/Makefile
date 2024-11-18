run: arreglo.exe
	./arreglo.exe

arreglo.exe: arreglo.c funciones.h funciones.o
	gcc arreglo.c funciones.o -o arreglo.exe

funciones.o: funciones.c
	gcc -c funciones.c -o funciones.o
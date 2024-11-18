run: contador.exe
	./contador.exe

run2: arreglos.exe
	./arreglos.exe

arreglos.exe: arreglos.c funciones.h funciones.o
	gcc arreglos.c funciones.o -o arreglos.exe

contador.exe: contador.c funciones.h funciones.o
	gcc contador.c funciones.o -o contador.exe

funciones.o: funciones.c
	gcc -c funciones.c -o funciones.o


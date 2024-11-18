run: conta.exe
	./conta.exe

run2: nobinario.exe
	./nobinario.exe

nobinario.exe: nobinario.c biblioteca.h funciones.h biblioteca.o funciones.o
	gcc nobinario.c biblioteca.o funciones.o -o nobinario.exe

funciones.o: funciones.c funciones.h
	gcc -c funciones.c -o funciones.o

conta.exe: conta.c biblioteca.h biblioteca.o
	gcc conta.c biblioteca.o -o conta.exe

biblioteca.o: biblioteca.c
	gcc -c biblioteca.c -o biblioteca.o
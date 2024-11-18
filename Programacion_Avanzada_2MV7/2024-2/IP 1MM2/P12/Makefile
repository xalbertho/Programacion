run: main.exe
	./main.exe

main.exe: main.c bliblioteca.h bliblioteca.o
	gcc main.c bliblioteca.o -o main.exe

bliblioteca.o: bliblioteca.c
	gcc -c bliblioteca.c -o bliblioteca.o
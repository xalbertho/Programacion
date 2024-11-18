run: main.exe
	./main.exe

main.exe: main.cpp biblioteca.hpp biblioteca.o
	g++ main.cpp biblioteca.o -o main.exe

biblioteca.o: biblioteca.cpp
	g++ -c biblioteca.cpp -o biblioteca.o
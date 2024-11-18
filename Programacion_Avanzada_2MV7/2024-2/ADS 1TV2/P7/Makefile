run: main.exe
	./main.exe

main.exe: main.cpp funciones.hpp funciones.o
	g++ main.cpp funciones.o -o main.exe

funciones.o: funciones.cpp
	g++ -c funciones.cpp -o funciones.o
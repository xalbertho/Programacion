run: main.exe
	./main.exe

main.exe: main2.cpp tools.hpp tools.o
	g++ main2.cpp tools.o -o main.exe

tools.o: tools.cpp
	g++ -c tools.cpp -o tools.o
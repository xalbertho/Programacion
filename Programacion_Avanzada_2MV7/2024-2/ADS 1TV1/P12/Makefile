run: main.exe
	./main.exe

main.exe: main.cpp agenda.hpp tools.hpp agenda.o tools.o
	g++ -std=c++11 main.cpp agenda.o tools.o -o main.exe

agenda.o: agenda.cpp agenda.hpp
	g++ -std=c++11 -c agenda.cpp -o agenda.o

tools.o: tools.cpp
	g++ -std=c++11 -c tools.cpp -o tools.o
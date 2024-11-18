SRC=agenda.c
APP=agenda.exe
run: $(APP)
	./$(APP)

$(APP): $(SRC) tools.h tools.o
	gcc $(SRC) tools.o -o $(APP)

tools.o: tools.c
	gcc -c tools.c -o tools.o
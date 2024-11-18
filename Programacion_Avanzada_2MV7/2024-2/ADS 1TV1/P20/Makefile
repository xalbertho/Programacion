APP=main.exe
SRC=main.cpp
HEAD=funciones.hpp
OBJ=funciones.o
FNSRC=funciones.cpp
run: $(APP)
	./$(APP)

$(APP): $(SRC) $(OBJ) $(HEAD)
	g++ $(SRC) $(OBJ) -o $(APP)

$(OBJ): $(HEAD) $(FNSRC)
	g++ -c $(FNSRC) -o $(OBJ)
APP=agenda.exe
MAIN=agenda.c
TOOLS=tools.c
TOOLS_H=tools.h
TOOLS_OBJ=tools.o
COMPILADOR=gcc
AGENDA=libagenda.c
AGENDA_H=libagenda.h
AGENDA_OBJ=libagenda.o

run: $(APP)
	./$(APP)

$(APP): $(MAIN) $(TOOLS_H) $(TOOLS_OBJ) $(AGENDA_OBJ)
	$(COMPILADOR) $(MAIN) $(TOOLS_OBJ) $(AGENDA_OBJ) -o $(APP)

$(TOOLS_OBJ): $(TOOLS) $(TOOLS_H)
	$(COMPILADOR) -c $(TOOLS) -o $(TOOLS_OBJ)

$(AGENDA_OBJ): $(AGENDA) $(AGENDA_H)
	$(COMPILADOR) -c $(AGENDA) -o $(AGENDA_OBJ)
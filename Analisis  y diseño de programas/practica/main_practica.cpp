#include "practica.hpp"

int main() {

    Torneo torneo;

    torneo.agregarDisciplina("Futbol");
    torneo.agregarDisciplina("Basketball");
    torneo.agregarDisciplina("Voleibol");

    torneo.registrarParticipante("Juan Perez", "Futbol");
    torneo.registrarParticipante("Maria Lopez", "Basketball");
    torneo.registrarParticipante("Carlos Garcia", "Voleibol");


    torneo.mostrarParticipantes();

    return 0;
}

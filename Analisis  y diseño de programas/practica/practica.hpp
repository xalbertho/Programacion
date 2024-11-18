
#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Disciplina {
public:
    string nombre;

    Disciplina(string nombre);
    string getNombre();
};


Disciplina::Disciplina(string nombre) {
    this->nombre = nombre;
}

string Disciplina::getNombre() {
    return nombre;
}

class Estudiante {
public:
    string nombre;
    Disciplina disciplina;

    Estudiante(string nombre, Disciplina disciplina);
    string getNombre();
    Disciplina getDisciplina();
};


Estudiante::Estudiante(string nombre, Disciplina disciplina)
    : disciplina(disciplina) {
    this->nombre = nombre;
}

string Estudiante::getNombre() {
    return nombre;
}

Disciplina Estudiante::getDisciplina() {
    return disciplina;
}

class Torneo {
public:
    vector<Estudiante> participantes;
    vector<Disciplina> disciplinas;

    void agregarDisciplina(string nombreDisciplina);
    void registrarParticipante(string nombreEstudiante, string nombreDisciplina);
    void mostrarParticipantes();
};


void Torneo::agregarDisciplina(string nombreDisciplina) {
    Disciplina nuevaDisciplina(nombreDisciplina);
    disciplinas.push_back(nuevaDisciplina);
}

void Torneo::registrarParticipante(string nombreEstudiante, string nombreDisciplina) {
    Disciplina disciplinaEncontrada(nombreDisciplina);
    for (int i = 0; i < disciplinas.size(); i++) {
        if (disciplinas[i].getNombre() == nombreDisciplina) {
            disciplinaEncontrada = disciplinas[i];
            break;
        }
    }

    Estudiante nuevoEstudiante(nombreEstudiante, disciplinaEncontrada);
    participantes.push_back(nuevoEstudiante);
}

void Torneo::mostrarParticipantes() {
    cout << "Participantes del Torneo:" << endl;
    for (int i = 0; i < participantes.size(); i++) {
        cout << "Nombre: " << participantes[i].getNombre() << ", Disciplina: " 
             << participantes[i].getDisciplina().getNombre() << endl;
    }
}


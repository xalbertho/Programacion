
#include<iostream>

using namespace std;

class Persona{
string nombre[10], nombre2;
int edad[10], edad2;

Persona(string, int);
void agregarProfesor(string,int);
void agregarAlumno();
void mostrarProfesores();
void mostrarAlumnos();

};

Persona::Persona(string n, int e){
    int contador=0;
    nombre[contador]=n;
    edad[contador]=e;
    contador++;
}

void Persona::agregarProfesor(string nombre,int edad){
    int contador=0;
    nombre[contador]=nombre;
    edad[contador]=edad;
    contador++;
}

class Persona: public Profesor{
    string Cedula[10];

    Profesor(string);
    void mostrarCedula();
};

Profesor::Profesor(string c){
    Cedula=c;
}

void Profesor::mostrarCedula(){
    cout<<"La cedula del profesor es: "<<Cedula<<endl;
}

class Persona: public Alumno{
    string matricula[10];

    Alumno(string);
    void mostrarMatricula();
};

Alumno::Alumno(string alum){
    cout<<"La matricula del alumno es: "<<matricula<<endl;
}

int main(){
    cout<<"Introduce nombre"<<endl;
    getline(cin, n1);
    cout<<"Introduce la edad"<<endl;
    cin>>e1;

    Persona p1(n1, e1);

    cout<<"Ingresa un profesor"<<endl;
    getline(cin, nom);

    p1.agregarProfesor();

}








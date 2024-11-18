#include "herencia.hpp"

main(){

	int numero, empleado;
	string c;

	cout << "Ingresa el numero de empleado" << endl;
	cin >> empleado;
	cout << "Ingresa el numero de boleta " << endl;
	cin >> numero;
	cout << "Ingresa la carrera que estudias en UPIITA:  " << endl;
	cin >> c;

	Estudiante e(numero, c);
	e.Muestra();
	Docente d(empleado);
	d.Mostrar();
}

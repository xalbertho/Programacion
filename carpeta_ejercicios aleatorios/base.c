#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NOMBRE 50

typedef struct {
    int numero;
    int contrasena;
    double saldo;
    char nombre[MAX_NOMBRE];
} Cuenta;

void crearBaseDeDatos() {
    FILE *archivo = fopen("basededatos.bd", "wb");
    if (!archivo) {
        perror("Error al crear el archivo de base de datos");
        exit(1);
    }

    // Ejemplo de cuentas
    Cuenta cuentas[] = {
        {1001, 1234, 1500.00, "Juan Perez"},
        {1002, 5678, 2500.50, "Maria Lopez"},
        {1003, 9101, 350.75, "Carlos Sanchez"}
    };

    int numCuentas = sizeof(cuentas) / sizeof(cuentas[0]);

    for (int i = 0; i < numCuentas; i++) {
        fwrite(&cuentas[i].numero, sizeof(int), 1, archivo);
        fwrite(&cuentas[i].contrasena, sizeof(int), 1, archivo);
        fwrite(&cuentas[i].saldo, sizeof(double), 1, archivo);
        fwrite(cuentas[i].nombre, sizeof(char), MAX_NOMBRE, archivo);
    }

    fclose(archivo);
    printf("Base de datos creada con %d cuentas.\n", numCuentas);
}

int main() {
    crearBaseDeDatos();
    return 0;
}

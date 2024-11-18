/**
 * @file cajero.c
 * @author {SalasTrujano Diego} ({diegosalastrujano2@gmail.com})
 * @brief 
 * @version 0.1
 * @date 2024-07-05
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_NOMBRE 50

typedef struct {
    int numero;
    int contrasena;
    double saldo;
    char nombre[MAX_NOMBRE];
} Cuenta;

void acceder(Cuenta *cuenta);
void cambiarContrasenia(Cuenta *cuenta);
void consultarSaldo(const Cuenta *cuenta);
void retirar(Cuenta *cuenta);
void depositar(Cuenta *cuenta);
void transferir(Cuenta *cuenta);
void basededatosActualizada(const Cuenta *cuenta);
void imprimirTicket(const char *operacion, const Cuenta *cuenta);

int main() {
    Cuenta cuenta;
    acceder(&cuenta);

    int opcion;
    do {
        printf("\nMenu\n");
        printf("1. Cambiar Contrasena\n");
        printf("2. Consultar Saldo\n");
        printf("3. Retirar\n");
        printf("4. Depositar\n");
        printf("5. Transferir\n");
        printf("6. Salir\n");
        printf("Seleccione una opcion: ");
        scanf("%d", &opcion);

        switch (opcion) {
            case 1:
                cambiarContrasenia(&cuenta);
                break;
            case 2:
                consultarSaldo(&cuenta);
                break;
            case 3:
                retirar(&cuenta);
                break;
            case 4:
                depositar(&cuenta);
                break;
            case 5:
                transferir(&cuenta);
                break;
            case 6:
                printf("Saliendo...\n");
                break;
            default:
                printf("Opcion invalida. Intente de nuevo.\n");
        }
    } while (opcion != 6);

    return 0;
}

void acceder(Cuenta *cuenta) {
    FILE *archivo = fopen("basededatos.bd", "rb");
    if (!archivo) {
        perror("Error al abrir el archivo de base de datos");
        exit(1);
    }

    int numCuenta, contrasena;
    printf("Ingrese su numero de cuenta: ");
    scanf("%d", &numCuenta);
    printf("Ingrese su contrasena: ");
    scanf("%d", &contrasena);

    int encontrado = 0;
    Cuenta cuentaTemp;
    while (fread(&cuentaTemp.numero, sizeof(int), 1, archivo) &&
           fread(&cuentaTemp.contrasena, sizeof(int), 1, archivo) &&
           fread(&cuentaTemp.saldo, sizeof(double), 1, archivo) &&
           fread(cuentaTemp.nombre, sizeof(char), MAX_NOMBRE, archivo)) {
        cuentaTemp.nombre[MAX_NOMBRE - 1] = '\0';

        if (cuentaTemp.numero == numCuenta && cuentaTemp.contrasena == contrasena) {
            *cuenta = cuentaTemp;
            encontrado = 1;
            break;
        }
    }

    fclose(archivo);

    if (!encontrado) {
        printf("Cuenta o contrasena incorrecta.\n");
        exit(1);
    }
}

void cambiarContrasenia(Cuenta *cuenta) {
    int contrasenaActual, nuevaContrasena;
    printf("Ingrese su contrasena actual: ");
    scanf("%d", &contrasenaActual);

    if (contrasenaActual != cuenta->contrasena) {
        printf("Contrasena incorrecta.\n");
        return;
    }

    printf("Ingrese su nueva contrasena: ");
    scanf("%d", &nuevaContrasena);

    if (nuevaContrasena == cuenta->contrasena || nuevaContrasena < 1000 || nuevaContrasena > 9999) {
        printf("Contrasena invalida.\n");
        return;
    }

    cuenta->contrasena = nuevaContrasena;
    basededatosActualizada(cuenta);
    imprimirTicket("Cambio de Contrasena", cuenta);
}

void consultarSaldo(const Cuenta *cuenta) {
    printf("Saldo actual: $%.2f\n", cuenta->saldo);
    imprimirTicket("Consulta de Saldo", cuenta);
}

void retirar(Cuenta *cuenta) {
    double monto;
    printf("Ingrese el monto a retirar: ");
    scanf("%lf", &monto);

    if (monto > cuenta->saldo) {
        printf("Saldo insuficiente.\n");
        return;
    }

    cuenta->saldo -= monto;
    basededatosActualizada(cuenta);
    imprimirTicket("Retiro", cuenta);
}

void depositar(Cuenta *cuenta) {
    double monto;
    printf("Ingrese el monto a depositar (multiplo de 20, maximo $15000): ");
    scanf("%lf", &monto);

    if (monto <= 0 || monto > 15000 || ((int)monto) % 20 != 0) {
        printf("Monto invalido.\n");
        return;
    }

    cuenta->saldo += monto;
    basededatosActualizada(cuenta);
    imprimirTicket("Deposito", cuenta);
}

void transferir(Cuenta *cuenta) {
    int cuentaDestino;
    double monto;
    printf("Ingrese el numero de cuenta del beneficiario: ");
    scanf("%d", &cuentaDestino);
    printf("Ingrese el monto a transferir: ");
    scanf("%lf", &monto);

    if (monto > cuenta->saldo) {
        printf("Saldo insuficiente.\n");
        return;
    }

    Cuenta cuentaDest;
    FILE *archivoLectura = fopen("basededatos.bd", "rb");
    FILE *archivoEscritura = fopen("temp.bd", "wb");
    int cuentaEncontrada = 0;

    while (fread(&cuentaDest.numero, sizeof(int), 1, archivoLectura) &&
           fread(&cuentaDest.contrasena, sizeof(int), 1, archivoLectura) &&
           fread(&cuentaDest.saldo, sizeof(double), 1, archivoLectura) &&
           fread(cuentaDest.nombre, sizeof(char), MAX_NOMBRE, archivoLectura)) {
        cuentaDest.nombre[MAX_NOMBRE - 1] = '\0';
        
        if (cuentaDest.numero == cuentaDestino) {
            cuentaDest.saldo += monto;
            cuentaEncontrada = 1;
        }
        fwrite(&cuentaDest.numero, sizeof(int), 1, archivoEscritura);
        fwrite(&cuentaDest.contrasena, sizeof(int), 1, archivoEscritura);
        fwrite(&cuentaDest.saldo, sizeof(double), 1, archivoEscritura);
        fwrite(cuentaDest.nombre, sizeof(char), MAX_NOMBRE, archivoEscritura);
    }

    fclose(archivoLectura);
    fclose(archivoEscritura);

    if (!cuentaEncontrada) {
        printf("Cuenta del beneficiario no encontrada.\n");
        remove("temp.bd");
        return;
    }

    remove("basededatos.bd");
    rename("temp.bd", "basededatos.bd");

    cuenta->saldo -= monto;
    basededatosActualizada(cuenta);
    imprimirTicket("Transferencia", cuenta);
}

void basededatosActualizada(const Cuenta *cuenta) {
    FILE *archivoLectura = fopen("basededatos.bd", "rb");
    FILE *archivoEscritura = fopen("temp.bd", "wb");
    Cuenta temp;

    while (fread(&temp.numero, sizeof(int), 1, archivoLectura) &&
           fread(&temp.contrasena, sizeof(int), 1, archivoLectura) &&
           fread(&temp.saldo, sizeof(double), 1, archivoLectura) &&
           fread(temp.nombre, sizeof(char), MAX_NOMBRE, archivoLectura)) {
        temp.nombre[MAX_NOMBRE - 1] = '\0';
        
        if (temp.numero == cuenta->numero) {
            fwrite(&cuenta->numero, sizeof(int), 1, archivoEscritura);
            fwrite(&cuenta->contrasena, sizeof(int), 1, archivoEscritura);
            fwrite(&cuenta->saldo, sizeof(double), 1, archivoEscritura);
            fwrite(cuenta->nombre, sizeof(char), MAX_NOMBRE, archivoEscritura);
        } else {
            fwrite(&temp.numero, sizeof(int), 1, archivoEscritura);
            fwrite(&temp.contrasena, sizeof(int), 1, archivoEscritura);
            fwrite(&temp.saldo, sizeof(double), 1, archivoEscritura);
            fwrite(temp.nombre, sizeof(char), MAX_NOMBRE, archivoEscritura);
        }
    }

    fclose(archivoLectura);
    fclose(archivoEscritura);

    remove("basededatos.bd");
    rename("temp.bd", "basededatos.bd");
}

void imprimirTicket(const char *operacion, const Cuenta *cuenta) {
    time_t t = time(NULL);
    struct tm tm = *localtime(&t);

    char nombreArchivo[100];
    snprintf(nombreArchivo, sizeof(nombreArchivo), "ticket_%s_%d-%02d-%02d_%02d-%02d-%02d.txt",
             cuenta->nombre, tm.tm_year + 1900, tm.tm_mon + 1, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec);

    FILE *ticket = fopen(nombreArchivo, "w");
    if (!ticket) {
        perror("Error al crear el ticket");
        return;
    }

    fprintf(ticket, "Operacion: %s\n", operacion);
    fprintf(ticket, "Fecha: %d-%02d-%02d %02d:%02d:%02d\n", tm.tm_year + 1900, tm.tm_mon + 1, tm.tm_mday,
            tm.tm_hour, tm.tm_min, tm.tm_sec);
    fprintf(ticket, "Numero de Cuenta: %d\n", cuenta->numero);
    fprintf(ticket, "Nombre: %s\n", cuenta->nombre);
    fprintf(ticket, "Saldo: %.2f\n", cuenta->saldo);

    fclose(ticket);
    printf("Ticket generado: %s\n", nombreArchivo);
}

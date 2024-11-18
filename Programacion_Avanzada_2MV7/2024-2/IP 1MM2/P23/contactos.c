/**
 * @file contactos.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-26
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

typedef int Entero;
typedef float F;

typedef struct Fecha
{
    int dia;
    int mes;
    int anio;
} Fecha;


typedef struct Contacto
{
    char nombre[500];
    char apodo[100];
    char telefono[30];
    char correo[100];
    Fecha fnacimiento;
} Contacto;

struct estructura
{
    int entero;
};


void imprimir(Contacto c) {
    printf("\nNombre: %s\nApodo: %s\nTelefono: %s\nCorreo: %s\n", c.nombre, c.apodo, c.telefono, c.correo);
    printf("Fecha de nacimiento: %02i/%02i/%04i\n", c.fnacimiento.dia, c.fnacimiento.mes, c.fnacimiento.anio);
}

int main()
{
    F variable;
    int entero;
    Fecha fecha;
    struct estructura variable;
    Contacto lista[100], martin;
    
    Contacto *cacho;

    cacho = (Contacto *)malloc(sizeof(Contacto));

    strcpy(cacho->nombre, "Valeria, Adi, Lara, Valeria2, Mia, Naomi, Dulce y Miriam (la casada)");
    strcpy(cacho->apodo, "Mi amor");
    strcpy(cacho->telefono, "55000001");
    strcpy(cacho->correo, "valeria@cecytem.edomex.mx");

    cacho->fnacimiento.dia = 27;
    cacho->fnacimiento.mes = 3;
    cacho->fnacimiento.anio = 2006;


    imprimir(*cacho);

    free(cacho);

    return 0;


    entero = 10;

    martin.fnacimiento.anio = 2005;
    martin.fnacimiento.mes = 3;
    martin.fnacimiento.dia = 17;

    strcpy(martin.nombre, "Franchesco Virgolini");
    strcpy(martin.apodo, "Martin");
    strcpy(martin.telefono, "50 y five");
    strcpy(martin.correo, "maquinadelmal2000@alumno.ipn.mx");

    imprimir(martin);


    return 0;
}

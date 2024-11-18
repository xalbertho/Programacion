/**
 * @file estructura.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-25
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef float flotante;
typedef int I;

typedef struct MiNumero
{
    int entero;
    float flotante;
    double doble;
} MiNumero;

typedef struct Fecha
{
    int dia;
    int mes;
    int anio;
} Fecha;


typedef struct Contacto
{
    char nombre[100];
    char apodo[50];
    char telefono[20];
    char correo[100];
    Fecha fnacimiento;
} Contacto;





int main()
{
    Contacto *contacto;
    contacto = (Contacto *)malloc(sizeof(Contacto));

    contacto->fnacimiento.anio = 2020;
    contacto->fnacimiento.mes = 12;
    contacto->fnacimiento.dia = 14;

    printf("Nombre: ");
    fgets(contacto->nombre, 100, stdin);

    //strcpy(contacto->nombre, "Tony");
    strcpy(contacto->apodo, "El que no esta");
    strcpy(contacto->telefono, "81683461872");
    strcpy(contacto->correo, "tony@elquenoesta.com");

    printf("Nombre: %s\nApodo: %s\nNumero: %s\nCorreo: %s\n", contacto->nombre, contacto->apodo, contacto->telefono, contacto->correo);

    printf("Fecha de nacimiento: %i/%i/%i\n", contacto->fnacimiento.dia, contacto->fnacimiento.mes, contacto->fnacimiento.anio);
    



    

    
    return 0;
}

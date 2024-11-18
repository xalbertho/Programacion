/**
 * @file agenda.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-03-19
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>
#include<string.h>

typedef struct Contacto
{
    char nombre[100];
    char apellido[100];
    char apodo[10];
    char numero[20];
} Contacto;

void llamar(Contacto c) {
    printf("Llamando a %s\n", c.apodo);
}


int main()
{
    int numContactos = 0;
    Contacto listaContactos[100];

    strcpy(listaContactos[0].apodo, "Josue");
    llamar(listaContactos[0]);




    return 0;
}

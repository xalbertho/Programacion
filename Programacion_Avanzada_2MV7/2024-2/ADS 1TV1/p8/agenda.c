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
    char numero[20];
    char apodo[50];
    void llamar(Contacto c){
    printf("Llamando a %s\n", c.apodo);
}

} Contacto;

typedef int Entero;




int main()
{
    Entero variable;
    Contacto listaContactos[100];

    strcpy(listaContactos[0].apodo, "Tux");

    llamar(listaContactos[0]);


    
    
    return 0;
}

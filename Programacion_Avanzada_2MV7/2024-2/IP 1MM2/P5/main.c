/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief IFs
 * @version 0.1
 * @date 2024-02-27
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int edad;
    printf("Usuario, ingrese su edad: ");
    scanf("%d", &edad);


    if(edad < 0) {
        printf("Edad con capacidades diferentes\n");
    } else if(edad >= 18 && edad <= 35) {
        printf("Eres el futuro de Mexico, te invitamos a votar este 7 de julio\n");
    } else if(edad > 35 && edad <= 50) {
        printf("Le sugerimos pasar por su apoyo del bienestar\n");
    } else if (edad >=51) {
        printf("La tierra te reclama :)\n");
    } else {
        printf("Vete a hacer tu tarea chamaco miau\n");
    }
    
    return 0;
}

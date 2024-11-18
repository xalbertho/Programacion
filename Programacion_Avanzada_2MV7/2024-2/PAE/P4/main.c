/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief IFs
 * @version 0.1
 * @date 2024-02-23
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
        printf("Edad con capacidades diferentes.\n");
    } else if(edad >= 18 && edad <= 25) {
        printf("Mi primera chamba.\n");
    } else if(edad >=26 && edad <= 40) {
        printf("Ya eres un anciano.\n");
    } else if(edad >= 41 && edad <= 70) {
        printf("Saca tu tarjeta Bienestar.\n");
    } else if(edad >= 71) {
        printf("Descana en paz.\n");
    } else {
        printf("No eres legal. Ve con tu mami.\n");
    }


    return 0;
}

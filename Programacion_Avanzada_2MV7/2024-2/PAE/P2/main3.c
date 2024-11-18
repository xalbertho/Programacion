/**
 * @file main3.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Manejo de entradas y salidas 3
 * @version 0.1
 * @date 2024-02-19
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int edad;
    float peso;
    int dia, mes, anio;
    char nombre[10];

    printf("Usuario, ingresa tu edad: ");
    scanf("%d", &edad);
    printf("Ahora, escribe tu nombre: ");
    getc(stdin);
    fgets(nombre, 10, stdin);
    printf("Ahora escribe tu peso: ");
    scanf("%f", &peso);
    printf("Ahora, escribe tu fecha de nacimiento en formato dd/mm/aa: ");
    scanf("%i/%i/%i", &dia, &mes, &anio);


    printf("Hola %s, tu edad es %i y tu peso es %015.2f\nTu fecha de nacimiento es: %02i-%02i-%02i", nombre, edad, peso, dia, mes, anio);





    return 0;
}

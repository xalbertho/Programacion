/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Ejemplo de manejo de entradas y salidas con formato
 * @version 0.1
 * @date 2024-02-19
 * 
 * 
 */
#include<stdio.h>
#define PI 3


int main()
{
    int edad = PI;
    float estatura;
    int dia, mes, anio;
    char nombre[10];

    printf("Usuario, ingresa tu edad: ");
    scanf("%d", &edad);

    printf("Ahora, ingresa tu nombre: ");
    getchar();
    fgets(nombre, 10, stdin);

    printf("Ahora, ingresa tu estatura: ");
    scanf("%f", &estatura);

    printf("Ahora, ingresa tu fecha de nacimiento en formato dia/mes/anio: ");
    scanf("%i/%i/%i", &dia, &mes, &anio);

    printf("Hola %s,\nTu edad es: %i\nTu estatura es: %15.4f", nombre, edad, estatura);
    printf("\nTu fecha de nacimiento es %02i-%02i-%02i", dia, mes, anio);

    return 0;
}

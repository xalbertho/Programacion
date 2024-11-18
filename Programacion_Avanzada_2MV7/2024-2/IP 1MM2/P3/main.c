/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Un programa
 * @version 0.1
 * @date 2024-02-20
 * 
 */
#include<stdio.h>
#define PI 4
#define PRINT printf("Hola %s naciste %02i-%02i-%02i\n", nombre, dia, mes, anio);

int global; // LO PEOR QUE PUEDE HACER EN SU VIDA 

int main()
{
    char nombre[10];
    int dia = PI,mes,anio;
    const int CONSTANTE = 5;

    //CONSTANTE = 7;


    {
        static int local;
    }

    printf("Usuario, ingrese su nombre o te pico: ", global);
    fgets(nombre, 10, stdin);

    printf("Ahora, ingrese su fecha de nacimiento en formato dd/mm/aa: ");
    scanf("%i/%i/%i", &dia, &mes, &anio);

    PRINT
    
    return 0;
}

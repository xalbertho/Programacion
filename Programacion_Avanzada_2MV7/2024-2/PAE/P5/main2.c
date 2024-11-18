/**
 * @file main2.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Programa que calcula el factorial de un numero
 * @version 0.1
 * @date 2024-02-26
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int numero;
    int factorial = 1;
    printf("Usuario, ingresa un numero entero positivo: ");
    scanf("%i", &numero);

    /*for (int i = 1; i <= numero; i++)
    {
        factorial *= i;
    }*/

    for (int i = numero; i > 0; i--)
    {
        factorial *= i;
    }

    printf("El fatorial de %i es %i\n", numero, factorial);
    
    return 0;
}

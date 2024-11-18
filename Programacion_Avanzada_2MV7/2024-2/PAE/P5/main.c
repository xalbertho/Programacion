/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Programa que solicite al usuario un numero
 * y devuleva la suma de sus digitos.
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
    int suma = 0;

    printf("Usuario, ingrese un numero entero positivo: ");
    scanf("%d", &numero);

    while(numero > 0) {
        suma = suma + (numero%10);
        numero = numero/10;
    }

    printf("La suma de los digitos es: %i\n", suma);
    return 0;
}

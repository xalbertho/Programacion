/**
 * @file contra.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-03-26
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include "biblioteca.h"

int main()
{
    int numero, contador = 0;
    printf("Usuario, ingresa un numero: ");
    scanf("%i", &numero);

    sumaDigitos(numero, &contador);

    printf("Suma de los digitos: %i\n", contador);
    return 0;
}

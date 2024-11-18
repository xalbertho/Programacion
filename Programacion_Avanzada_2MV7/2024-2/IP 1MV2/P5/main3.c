/**
 * @file main3.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-02-26
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>

int main()
{
    int numero;
    int factorial = 1;

    printf("Usuario, ingrese un numero entero positivo mayor a 0: ");
    scanf("%d", &numero);

    for (int i = numero; i > 0; i--)
    {
        factorial *= i;
    }

    printf("El factorial de %d es %d\n", numero, factorial);

    return 0;
}

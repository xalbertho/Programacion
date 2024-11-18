/**
 * @file contador.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-03-25
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>

void funcion_contador(int numero, int i)
{
    if ( i <= numero)
    {
        printf("%i ", i);
        i++;
        funcion_contador(numero, i);
    }
}

void funcion_contador_2(int numero)
{
    static int i = 0;
    if ( i <= numero)
    {
        printf("%i ", i);
        i++;
        funcion_contador_2(numero);
    }
}

int main()
{
    int numero;
    printf("Usuario, ingrese un numero: ");
    scanf("%i", &numero);

    funcion_contador_2(numero);

    return 0;
}
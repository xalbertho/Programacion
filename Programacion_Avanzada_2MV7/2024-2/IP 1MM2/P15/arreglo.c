/**
 * @file arreglo.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-03-26
 *
 * @copyright Copyright (c) 2024
 *
 */
#include "funciones.h"
#include <stdlib.h>
#include <time.h>
#include <stdio.h>
#define N 20

int main()
{
    int arreglo[N];
    srand(time(NULL));

    generar(arreglo, N);

    imprimir(arreglo, N);

    printf("\nEl elemento mas grande es: %i\n", elmasgrande(arreglo, N));

    return 0;
}

/**
 * @file nobinario.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-03-27
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "funciones.h"
#include "biblioteca.h"

#define N 10

int main()
{
    int arr[N], x, res = -1;
    srand(time(NULL));

    printf("Usuario, ingrese un valor entero positivo: ");
    scanf("%i", &x);

    generar(arr, N);
    ordena(arr, N);

    busquedaBinaria(arr, 0, N-1, x, &res);

    imprimir(arr, N);
    printf("\nEl valor %i %s se encuentra", x, ((res == -1) ? "NO" : "SI"));

    return 0;
}

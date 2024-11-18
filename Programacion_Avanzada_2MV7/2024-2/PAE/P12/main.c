/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-10
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "recursion.h"
#define N 10


int main()
{
    int arr[N], x, inicio = 0, final = N - 1, miche;

    srand(time(NULL));
    for (int i = 0; i < N; i++)
    {
        arr[i] = rand() % 101;
    }

    printf("Usuario, ingrese un numero a buscar: ");
    scanf("%i", &x);

    burburja(arr, N);
    imprime(arr, N);

    busca(arr, inicio, final, x) == -1 ? printf("No se encontro\n") : printf("SI se encontro\n");

    return 0;
}

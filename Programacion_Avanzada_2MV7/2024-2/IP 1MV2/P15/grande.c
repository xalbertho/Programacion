/**
 * @file arreglo.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-03-25
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 10

void generar(int *arr, int n)
{
    static int i = 0;
    if (i < n)
    {
        arr[i] = rand() % (N*100);
        i++;
        generar(arr, n);
    }
}

void imprime(int arr[], int n)
{
    static int i = 0;
    if (i < n)
    {
        printf("%i ", arr[i]);
        i++;
        imprime(arr, n);
    }
}

int elMasGrande(int *arr, int n)
{
    static int theBigOne = INT32_MIN;
    static int i = 0;
    if (i < n)
    {
        if (arr[i] > theBigOne)
            theBigOne = arr[i];

        i++;
        return elMasGrande(arr, n);
    }
    else
        return theBigOne;
}

int main()
{
    int arr[N];
    srand(time(NULL));

    generar(arr, N);

    imprime(arr, N);

    printf("\nEl elemento mas grande es: %i\n", elMasGrande(arr, N));

    return 0;
}

/**
 * @file recursion.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-12
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

void imprime(int *arr, int n)
{
    printf("\n[ ");
    for (int i = 0; i < n; i++)
    {
        printf("%i ", arr[i]);
    }
    printf("]\n");
}

void burburja(int *arr, int n)
{
    int aux;
    for (int j = 0; j < n; j++)
    {
        for (int i = 0; i < n - 1 - j; i++)
        {
            if (arr[i] > arr[i + 1])
            {
                aux = arr[i + 1];
                arr[i + 1] = arr[i];
                arr[i] = aux;
            }
        }
    }
}

int busca(int *arr, int inicio, int final, int x)
{
    int miche = 0;
    int indice = -1;
    if (final >= inicio)
    {
        miche = (inicio + final) / 2;
        if (arr[miche] == x)
        {
            indice = miche;
            return indice;
        }
        else if (arr[miche] < x)
        {
            inicio = miche + 1;
        }
        else
        {
            final = miche - 1;
        }
        return busca(arr, inicio, final, x);
    }

    return indice;
}

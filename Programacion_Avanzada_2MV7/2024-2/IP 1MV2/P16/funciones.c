/**
 * @file funciones.h
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-03-26
 *
 * @copyright Copyright (c) 2024
 *
 */
#include<stdlib.h>
#include<stdio.h>

void noDigitos(unsigned long numero, unsigned long *contador)
{
    if (numero > 0)
    {
        numero /= 10;
        (*contador)++;
        noDigitos(numero, contador);
    }
}

void sumaDigitos(unsigned long numero, unsigned long *suma)
{
    if (numero > 0)
    {
        (*suma) += numero % 10;
        numero /= 10;
        sumaDigitos(numero, suma);
    }
}

void burbuja(int *arr, int n)
{
    int aux;
    for (int j = 0; j < n; j++)
    {
        for (int i = 0; i < n - 1 - j; i++)
        {
            if (arr[i] > arr[i + 1])
            {
                aux = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = aux;
            }
        }
    }
}

void generar(int *arr, int n)
{
    static int i = 0;
    if (i < n)
    {
        arr[i] = rand() % (n*100);
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
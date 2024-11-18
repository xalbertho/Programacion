/**
 * @file funciones.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Codigo de mi biblioteca de funciones
 * @version 0.1
 * @date 2024-03-26
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>

void generar(int *arreglo, int n)
{
    static int i = 0;

    if (i < n)
    {
        arreglo[i] = rand() % (n);
        i++;
        generar(arreglo, n);
    }
}

void imprimir(int arreglo[], int n)
{
    static int i = 0;
    if (i < n)
    {
        printf("%i ", arreglo[i]);
        i++;
        imprimir(arreglo, n);
    }
    else
    {
        i = 0;
    }
}

int elmasgrande(int *arreglo, int n)
{
    static int j = 0;
    static int i = 0;
    if (i < n)
    {
        if (arreglo[j] < arreglo[i])
            j = i;
        i++;
        return elmasgrande(arreglo, n);
    }
    return arreglo[j];
}
/**
 * @file agenda.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-05-03
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

void agregar(double **arr, int *cont, double valor)
{
    if (*arr == NULL)
    {
        *arr = malloc(sizeof(double));
        *(*arr + 0) = valor;
        (*cont)++;
    }
    else
    {
        *arr = realloc(*arr, (*cont + 1) * sizeof(double));
        *(*arr + *cont) = valor;
        (*cont)++;
    }
}

void imprimir(double *arr, int cont)
{
    printf("\n[ ");
    for (int i = 0; i < cont; i++)
    {
        printf("%.2f ", *(arr + i));
    }
    printf("]\n");
}

bool eliminar(double **arr, int *cont, int indice)
{
    if (*arr == NULL)
    {
        return false;
    }
    else
    {
        if (indice < 0 || indice >= *cont)
        {
            return false;
        }
        else
        {
            if (*cont == 1)
            {
                free(*arr);
                *cont = 0;
                *arr = NULL;
                return true;
            }
            else
            {
                memcpy(*arr + indice, *arr + indice + 1, (*cont - indice - 1) * sizeof(double));
                *arr = realloc(*arr, (*cont - 1) * sizeof(double));
                (*cont)--;
                return true;
            }
        }
    }
}

int main()
{
    double *arreglo = NULL;
    int cont = 0;

    agregar(&arreglo, &cont, 8.8);
    agregar(&arreglo, &cont, 6.66);
    agregar(&arreglo, &cont, 7.77);
    agregar(&arreglo, &cont, 3.33);
    agregar(&arreglo, &cont, 9.99);

    imprimir(arreglo, cont);

    printf("%s\n", eliminar(&arreglo, &cont, 2) ? "Eliminado" : "No eliminado");
    imprimir(arreglo, cont);
    printf("%s\n", eliminar(&arreglo, &cont, 2) ? "Eliminado" : "No eliminado");
    imprimir(arreglo, cont);
    printf("%s\n", eliminar(&arreglo, &cont, 2) ? "Eliminado" : "No eliminado");
    imprimir(arreglo, cont);
    printf("%s\n", eliminar(&arreglo, &cont, 2) ? "Eliminado" : "No eliminado");
    imprimir(arreglo, cont);
    printf("%s\n", eliminar(&arreglo, &cont, 2) ? "Eliminado" : "No eliminado");
    imprimir(arreglo, cont);
    printf("%s\n", eliminar(&arreglo, &cont, 2) ? "Eliminado" : "No eliminado");
    imprimir(arreglo, cont);

    printf("%s\n", eliminar(&arreglo, &cont, 2) ? "Eliminado" : "No eliminado");
    imprimir(arreglo, cont);
    printf("%s\n", eliminar(&arreglo, &cont, 1) ? "Eliminado" : "No eliminado");
    imprimir(arreglo, cont);
    printf("%s\n", eliminar(&arreglo, &cont, 0) ? "Eliminado" : "No eliminado");
    imprimir(arreglo, cont);

    printf("%s\n", eliminar(&arreglo, &cont, 0) ? "Eliminado" : "No eliminado");
    imprimir(arreglo, cont);

    agregar(&arreglo, &cont, 7.69);
    imprimir(arreglo, cont);

    free(arreglo);

    return 0;
}

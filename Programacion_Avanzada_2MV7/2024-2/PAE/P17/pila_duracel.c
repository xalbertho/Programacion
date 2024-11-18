/**
 * @file pila_duracel.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-26
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool no_hay_naiden(int *pila)
{
    if (pila == NULL)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void enpilar(int **pila, int *cont, int valor)
{
    if (no_hay_naiden(*pila))
    {
        *pila = malloc(sizeof(int));
        **pila = valor;
        *cont = 1;
    }
    else
    {
        *pila = realloc(*pila, (*cont + 1) * sizeof(int));
        *(*pila + *cont) = valor;
        (*cont)++;
    }
}

void imprimir(int *pila, int cont)
{
    printf("[ ");
    for (int i = 0; i < cont; i++)
    {
        printf("%i ", *(pila + i));
    }
    printf("]\n");
}

bool desempilar(int **pila, int *cont, int *valor)
{
    if (no_hay_naiden(*pila))
    {
        return false;
    }
    else
    {
        if (*cont == 1)
        {
            *valor = **pila;
            free(*pila);
            *pila = NULL;
            *cont = 0;
        }
        else
        {
            *valor = *(*pila + (*cont-1));
            *pila = realloc(*pila, (*cont - 1) * sizeof(int));
            (*cont)--;
        }
        return true;
    }
}

int main()
{
    int *pila = NULL;
    int cont = 0;
    int valor;

    enpilar(&pila, &cont, 10);
    enpilar(&pila, &cont, 1);
    enpilar(&pila, &cont, 3);
    enpilar(&pila, &cont, 4);
    enpilar(&pila, &cont, 7);

    imprimir(pila, cont);

    if (desempilar(&pila, &cont, &valor))
        printf("Valor desempilado: %i\n", valor);
    else
        printf("No hay pila\n");

    imprimir(pila, cont);

    if (desempilar(&pila, &cont, &valor))
        printf("Valor desempilado: %i\n", valor);
    else
        printf("No hay pila\n");

    imprimir(pila, cont);
    if (desempilar(&pila, &cont, &valor))
        printf("Valor desempilado: %i\n", valor);
    else
        printf("No hay pila\n");

    imprimir(pila, cont);
    if (desempilar(&pila, &cont, &valor))
        printf("Valor desempilado: %i\n", valor);
    else
        printf("No hay pila\n");
    imprimir(pila, cont);
    if (desempilar(&pila, &cont, &valor))
        printf("Valor desempilado: %i\n", valor);
    else
        printf("No hay pila\n");
    imprimir(pila, cont);
    if (desempilar(&pila, &cont, &valor))
        printf("Valor desempilado: %i\n", valor);
    else
        printf("No hay pila\n");
    imprimir(pila, cont);
    if (desempilar(&pila, &cont, &valor))
        printf("Valor desempilado: %i\n", valor);
    else
        printf("No hay pila\n");
    imprimir(pila, cont);
    if (desempilar(&pila, &cont, &valor))
        printf("Valor desempilado: %i\n", valor);
    else
        printf("No hay pila\n");
    imprimir(pila, cont);
    if (desempilar(&pila, &cont, &valor))
        printf("Valor desempilado: %i\n", valor);
    else
        printf("No hay pila\n");
    imprimir(pila, cont);
    if (desempilar(&pila, &cont, &valor))
        printf("Valor desempilado: %i\n", valor);
    else
        printf("No hay pila\n");
    imprimir(pila, cont);
    if (desempilar(&pila, &cont, &valor))
        printf("Valor desempilado: %i\n", valor);
    else
        printf("No hay pila\n");
    imprimir(pila, cont);
    if (desempilar(&pila, &cont, &valor))
        printf("Valor desempilado: %i\n", valor);
    else
        printf("No hay pila\n");
    imprimir(pila, cont);
    return 0;
}

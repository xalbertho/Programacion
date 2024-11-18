/**
 * @file lifo.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-23
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool esta_vacia(int *pila)
{
    if (pila == NULL)
        return true;
    else
        return false;
}

void agregar(int **pila, int *cont, int valor)
{
    if (esta_vacia(*pila))
    {
        *pila = calloc(1, sizeof(int));
        **pila = valor;
        *cont = 1;
    }
    else
    {
        *pila = realloc(*pila, (*cont + 1) * sizeof(int));
        *(*pila + *cont) = valor;
        *cont = *cont + 1;
    }
}

bool despilar(int **pila, int *cont, int *valor)
{
    if (esta_vacia(*pila))
    {
        return false;
    }
    else
    {
        if (*cont == 1)
        {
            *valor = *(*pila);
            free(*pila);
            *cont = 0;
            *pila = NULL;
        }
        else
        {
            *valor = *(*pila + (*cont - 1));
            *pila = realloc(*pila, (*cont - 1) * sizeof(int));
            (*cont)--;
        }
        return true;
    }
}

void imprimir(int **pila, int cont)
{
    printf("[ ");
    for (int i = 0; i < cont; i++)
    {
        printf("%i ", *(*pila + i));
    }
    printf("]\n");
}

int main()
{
    int *pila = NULL;
    int cont = 0;
    int valor, i = 0;

    agregar(&pila, &cont, 1);
    agregar(&pila, &cont, 2);
    agregar(&pila, &cont, 3);
    agregar(&pila, &cont, 8);

    imprimir(&pila, cont);

    printf("\n");

    while (i < 10)
    {

        if (despilar(&pila, &cont, &valor))
        {
            printf("\nValor despilado: %i\n", valor);
            imprimir(&pila, cont);
        }
        else
        {
            printf("\nPila despilada\n");
            imprimir(&pila, cont);
        }
        i++;
    }

    return 0;
}

/**
 * @file fifo.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-24
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool esta_vacia(int *cola)
{
    if (cola == NULL)
        return true;
    else
        return false;
}

void agregar(int **cola, int *cont, int valor)
{
    if (esta_vacia(*cola))
    {
        *cola = calloc(1, sizeof(int));
        **cola = valor;
        *cont = 1;
    }
    else
    {
        *cola = realloc(*cola, (*cont + 1) * sizeof(int));
        *(*cola + *cont) = valor;
        *cont = *cont + 1;
    }
}

bool descolar(int **cola, int *cont, int *valor)
{
    if (esta_vacia(*cola))
    {
        return false;
    }
    else
    {
        if (*cont == 1)
        {
            *valor = *(*cola);
            free(*cola);
            *cont = 0;
            *cola = NULL;
        }
        else
        {
            *valor = **cola;
            for (int i = 1; i < *cont; i++)
            {
                *(*cola + (i - 1)) = *(*cola + i);
            }

            *cola = realloc(*cola, (*cont - 1) * sizeof(int));
            (*cont)--;
        }
        return true;
    }
}

void imprimir(int **cola, int cont)
{
    printf("[ ");
    for (int i = 0; i < cont; i++)
    {
        printf("%i ", *(*cola + i));
    }
    printf("]\n");
}

int main()
{
    int *cola = NULL;// Ponemos NULL
    int cont = 0;
    int valor, i = 0;

    agregar(&cola, &cont, 1);
    agregar(&cola, &cont, 2);
    agregar(&cola, &cont, 3);
    agregar(&cola, &cont, 8);

    imprimir(&cola, cont);

    printf("\n");

    while (i < 10)
    {

        if (descolar(&cola, &cont, &valor))
        {
            printf("\nValor descolado: %i\n", valor);
            imprimir(&cola, cont);
        }
        else
        {
            printf("\nCola descolada\n");
            imprimir(&cola, cont);
        }
        i++;
    }

    return 0;
}

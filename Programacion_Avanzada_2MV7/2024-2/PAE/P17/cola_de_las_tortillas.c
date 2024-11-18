/**
 * @file cola_de_las_tortillas.c
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

bool no_hay_naiden(int *cola)
{
    if (cola == NULL)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void enpilar(int **cola, int *cont, int valor)
{
    if (no_hay_naiden(*cola))
    {
        *cola = malloc(sizeof(int));
        **cola = valor;
        *cont = 1;
    }
    else
    {
        *cola = realloc(*cola, (*cont + 1) * sizeof(int));
        *(*cola + *cont) = valor;
        (*cont)++;
    }
}

void imprimir(int *cola, int cont)
{
    printf("[ ");
    for (int i = 0; i < cont; i++)
    {
        printf("%i ", *(cola + i));
    }
    printf("]\n");
}

bool desempilar(int **cola, int *cont, int *valor)
{
    if (no_hay_naiden(*cola))
    {
        return false;
    }
    else
    {
        if (*cont == 1)
        {
            *valor = **cola;
            free(*cola);
            *cola = NULL;
            *cont = 0;
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

int main()
{
    int *cola = NULL;
    int cont = 0;
    int valor;

    enpilar(&cola, &cont, 10);
    enpilar(&cola, &cont, 1);
    enpilar(&cola, &cont, 3);
    enpilar(&cola, &cont, 4);
    enpilar(&cola, &cont, 7);

    imprimir(cola, cont);

    if (desempilar(&cola, &cont, &valor))
        printf("Valor desencolado: %i\n", valor);
    else
        printf("No hay cola\n");

    imprimir(cola, cont);

    if (desempilar(&cola, &cont, &valor))
        printf("Valor desencolado: %i\n", valor);
    else
        printf("No hay cola\n");

    imprimir(cola, cont);
    if (desempilar(&cola, &cont, &valor))
        printf("Valor desencolado: %i\n", valor);
    else
        printf("No hay cola\n");

    imprimir(cola, cont);
    if (desempilar(&cola, &cont, &valor))
        printf("Valor desencolado: %i\n", valor);
    else
        printf("No hay cola\n");
    imprimir(cola, cont);
    if (desempilar(&cola, &cont, &valor))
        printf("Valor desencolado: %i\n", valor);
    else
        printf("No hay cola\n");
    imprimir(cola, cont);
    if (desempilar(&cola, &cont, &valor))
        printf("Valor desencolado: %i\n", valor);
    else
        printf("No hay cola\n");
    imprimir(cola, cont);
    if (desempilar(&cola, &cont, &valor))
        printf("Valor desencolado: %i\n", valor);
    else
        printf("No hay cola\n");
    imprimir(cola, cont);
    if (desempilar(&cola, &cont, &valor))
        printf("Valor desencolado: %i\n", valor);
    else
        printf("No hay cola\n");
    imprimir(cola, cont);
    if (desempilar(&cola, &cont, &valor))
        printf("Valor desencolado: %i\n", valor);
    else
        printf("No hay cola\n");
    imprimir(cola, cont);
    if (desempilar(&cola, &cont, &valor))
        printf("Valor desencolado: %i\n", valor);
    else
        printf("No hay cola\n");
    imprimir(cola, cont);
    if (desempilar(&cola, &cont, &valor))
        printf("Valor desencolado: %i\n", valor);
    else
        printf("No hay cola\n");
    imprimir(cola, cont);
    if (desempilar(&cola, &cont, &valor))
        printf("Valor desencolado: %i\n", valor);
    else
        printf("No hay cola\n");
    imprimir(cola, cont);
    return 0;
}

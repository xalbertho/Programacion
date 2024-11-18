/**
 * @file pila.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-22
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

void encolar(int **pila, int *cont, int valor)
{
    if (esta_vacia(*pila))
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

void imprime(int **pila, int cont)
{
    printf("\n[ ");
    for (int i = 0; i < cont; i++)
    {
        printf("%i ", *(*pila + i));
    }
    printf("]\n");
}

bool desenpilacion(int **pila, int *cont, int *valor)
{
    if (esta_vacia(*pila))
    {
        return false;
    }
    else
    {
        if (*cont == 1)
        {
            *valor = **pila;
            (*cont)--;
            free(*pila);
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

int main()
{
    int *pila = NULL;
    int cont = 0;
    int ultimo_valor;

    encolar(&pila, &cont, 1);
    encolar(&pila, &cont, 2);
    encolar(&pila, &cont, 3);
    encolar(&pila, &cont, 4);
    encolar(&pila, &cont, 5);

    imprime(&pila, cont);
    printf("Valor desenpilado: %i", desenpilacion(&pila, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&pila, cont);
    printf("Valor desenpilado: %i", desenpilacion(&pila, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&pila, cont);
    printf("Valor desenpilado: %i", desenpilacion(&pila, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&pila, cont);
    printf("Valor desenpilado: %i", desenpilacion(&pila, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&pila, cont);
    printf("Valor desenpilado: %i", desenpilacion(&pila, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&pila, cont);
    printf("Valor desenpilado: %i", desenpilacion(&pila, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&pila, cont);
    printf("Valor desenpilado: %i", desenpilacion(&pila, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&pila, cont);
    printf("Valor desenpilado: %i", desenpilacion(&pila, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&pila, cont);
    printf("Valor desenpilado: %i", desenpilacion(&pila, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&pila, cont);
    printf("Valor desenpilado: %i", desenpilacion(&pila, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&pila, cont);
    printf("Valor desenpilado: %i", desenpilacion(&pila, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&pila, cont);

    return 0;
}

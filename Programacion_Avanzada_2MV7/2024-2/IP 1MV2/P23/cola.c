/**
 * @file cola.c
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

bool esta_vacia(int *cola)
{
    if (cola == NULL)
        return true;
    else
        return false;
}

void encolar(int **cola, int *cont, int valor)
{
    if (esta_vacia(*cola))
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

void imprime(int **cola, int cont)
{
    printf("\n[ ");
    for (int i = 0; i < cont; i++)
    {
        printf("%i ", *(*cola + i));
    }
    printf("]\n");
}

bool desenpilacion(int **cola, int *cont, int *valor)
{
    if (esta_vacia(*cola))
    {
        return false;
    }
    else
    {
        *valor = **cola;
        if (*cont == 1)
        {
            (*cont)--;
            free(*cola);
            *cola = NULL;
        }
        else
        {
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
    int ultimo_valor;

    encolar(&cola, &cont, 1);
    encolar(&cola, &cont, 2);
    encolar(&cola, &cont, 3);
    encolar(&cola, &cont, 4);
    encolar(&cola, &cont, 5);

    imprime(&cola, cont);
    printf("Valor desencolado: %i", desenpilacion(&cola, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&cola, cont);
    printf("Valor desencolado: %i", desenpilacion(&cola, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&cola, cont);
    printf("Valor desencolado: %i", desenpilacion(&cola, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&cola, cont);
    printf("Valor desencolado: %i", desenpilacion(&cola, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&cola, cont);
    printf("Valor desencolado: %i", desenpilacion(&cola, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&cola, cont);
    printf("Valor desencolado: %i", desenpilacion(&cola, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&cola, cont);
    printf("Valor desencolado: %i", desenpilacion(&cola, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&cola, cont);
    printf("Valor desencolado: %i", desenpilacion(&cola, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&cola, cont);
    printf("Valor desencolado: %i", desenpilacion(&cola, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&cola, cont);
    printf("Valor desencolado: %i", desenpilacion(&cola, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&cola, cont);
    printf("Valor desencolado: %i", desenpilacion(&cola, &cont, &ultimo_valor) ? ultimo_valor : -1);
    imprime(&cola, cont);

    return 0;
}

/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-03-26
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include "funciones.h"
#include <stdlib.h>
#include <time.h>
#define N 100

int main()
{
    int arr[N], inf = 0, sup = N - 1, micha, x, idx = -1;
    srand(time(NULL));
    printf("Usuario, ingres un numero a buscar: ");
    scanf("%i", &x);

    generar(arr, N);
    burbuja(arr, N);
    imprime(arr, N);

    while (sup > inf)
    {
        micha = inf + ((sup - inf) / 2);
        if (arr[micha] == x)
        {
            idx = micha;
            break;
        }
        else if (x > arr[micha])
        {
            inf = micha + 1;
        }
        else
        {
            sup = micha - 1;
        }
    }

    printf("\nEl numero %s\n", ((idx < 0)?"NO esta":"SI esta"));

    return 0;
}

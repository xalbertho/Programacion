/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Burbuja, Bombon y Bellota
 * @version 0.1
 * @date 2024-03-05
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 100

int main()
{
    int arrg[N];
    int aux;
    srand(time(NULL));

    for (int i = 0; i < N; i++)
    {
        arrg[i] = rand()%N;
    }

    for (int i = 0; i < N; i++)
    {
        printf("%i ", arrg[i]);
    }

    // Ordenamos por Burbuja
    for (int j = 0; j < N - 1; j++)
    {
        for (int i = 0; i < N - 1 - j; i++)
        {
            if (arrg[i] < arrg[i + 1])
            {
                aux = arrg[i + 1];
                arrg[i + 1] = arrg[i];
                arrg[i] = aux;
            }
        }
    }

    printf("\n");
    for (int i = 0; i < N; i++)
    {
        printf("%i ", arrg[i]);
    }

    return 0;
}

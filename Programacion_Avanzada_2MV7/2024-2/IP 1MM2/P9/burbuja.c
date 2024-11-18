/**
 * @file burbuja.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Las chicas super poderosas (Bonbon, Bellota y BURBUJA)
 * @version 0.1
 * @date 2024-03-06
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 1500

int main()
{
    int rawr[N], aux;

    srand(time(NULL));

    for (int i = 0; i < N; i++)
    {
        rawr[i] = rand() % 100;
    }

    for (int i = 0; i < N; i++)
    {
        printf("%i ", rawr[i]);
    }

    // Empieza la burbuja
    for (int j = 0; j < N; j++)
    {
        for (int i = 0; i < N - 1 - j; i++)
        {
            if (rawr[i] > rawr[i + 1])
            {
                aux = rawr[i];
                rawr[i] = rawr[i + 1];
                rawr[i + 1] = aux;
            }
        }
    }

    printf("\n");

    for (int i = 0; i < N; i++)
    {
        printf("%i ", rawr[i]);
    }

    return 0;
}

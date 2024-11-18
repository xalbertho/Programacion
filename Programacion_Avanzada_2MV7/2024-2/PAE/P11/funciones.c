/**
 * @file funciones.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-03-27
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void genera(int *arrg, int n)
{
    
    static int i = 0;
    if (i < n)
    {
        arrg[i] = rand() % 51;
        i++;
        genera(arrg, n);
    }
}

void imprime(int arrg[], int n)
{
    static int i = 0;
    if (i < n)
    {
        printf("%i ", arrg[i]);
        i++;
        imprime(arrg, n);
    }
}

void cuenta(int n, int i)
{

    if (i <= n)
    {
        printf("%i ", i);
        i++;
        cuenta(n, i);
    }
}

void cuenta2(int n)
{
    static int i = 0;
    if (i <= n)
    {
        printf("%i ", i);
        i++;
        cuenta2(n);
    }
}

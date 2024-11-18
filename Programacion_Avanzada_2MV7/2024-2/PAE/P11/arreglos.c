/**
 * @file arreglos.c
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
#include"funciones.h"

#define N 10





int main()
{
    int arrg[N];
    srand(time(NULL));

    genera(arrg, N);

    imprime(arrg, N);

    return 0;
}

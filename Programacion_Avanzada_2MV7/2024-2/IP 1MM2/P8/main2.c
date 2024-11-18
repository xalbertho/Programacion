/**
 * @file main2.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Ejemplo de arreglos
 * @version 0.1
 * @date 2024-03-05
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define N 1000

int main()
{
    int arrg[N];
    srand(time(NULL));

    for (int i = 0; i < N; i++)
    {
        arrg[i] = (rand()%4951)+50;
    }


    for (int i = 0; i < N; i++)
    {
        printf("%i\n", arrg[i]);    
    }
    
    return 0;
}

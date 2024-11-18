/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Ejemplo de arreglos
 * @version 0.1
 * @date 2024-03-04
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define N 100

int main()
{
    int arr[N];

    srand(time(NULL));
    for (int i = 0; i < N; i++)
    {
        arr[i] = (rand()%150)+51;
    }
    
    

    for (int i = 0; i < N; i++)
    {
        printf("%i ", arr[i]);
    }
    
    return 0;
}

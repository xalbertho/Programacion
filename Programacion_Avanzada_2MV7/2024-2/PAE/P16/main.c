/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-22
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int* generadorDeArreglo() {
    int arr[5];
    int *a = arr;
    for (int i = 0; i < 5; i++)
    {
        *(arr+i) = i+1;
    }
    return a;
}

int main()
{
    int *arr = generadorDeArreglo();

    for (int i = 0; i < 5; i++)
    {
        printf("%i ", *(arr+i));
    }
    
    return 0;
}

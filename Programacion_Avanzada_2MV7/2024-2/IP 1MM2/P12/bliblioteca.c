/**
 * @file bliblioteca.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Mi segunda bliblioteca de funciones 
 * @version 0.1
 * @date 2024-03-20
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

void imprime(int *arr, int size) {
    printf("[ ");
    for (int i = 0; i < size; i++)
    {
        printf("%i ", arr[i]);
    }
    printf("]\n");
}


void burbuja(int *arr, int size)
{
    int aux;
    for (int j = 0; j < size; j++)
    {
        for (int i = 0; i < size - 1 - j; i++)
        {
            if (arr[i] > arr[i + 1])
            {
                aux = arr[i + 1];
                arr[i + 1] = arr[i];
                arr[i] = aux;
            }
        }
    }
}

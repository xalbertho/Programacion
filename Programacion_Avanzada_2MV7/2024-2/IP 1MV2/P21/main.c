/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-16
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>

int* prueba(int n) {
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        arr[i] = i;
    }
    return arr;
}

int main()
{
    int *arr = prueba(7);

    for (size_t i = 0; i < 7; i++)
    {
        printf("%i ", arr[i]);
    }
    
    
    return 0;
}

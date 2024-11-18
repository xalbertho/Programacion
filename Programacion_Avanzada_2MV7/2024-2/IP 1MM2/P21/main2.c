/**
 * @file main2.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-17
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int* gen_arr() {
    int arr[5] = {1,2,3,4,5};
    return arr;
}

int main()
{
    int *arreglo = gen_arr();

    for (int i = 0; i < 5; i++)
    {
        printf("%i ", arreglo[i]);
    }
    
    
    return 0;
}

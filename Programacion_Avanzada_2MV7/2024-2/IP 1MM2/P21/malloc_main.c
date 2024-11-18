/**
 * @file malloc_main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-17
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
    int *arr = (int*) calloc(5, sizeof(int));
    arr[0] = 87;
    arr[1] = 25;
    printf("%p - %i\n", arr, *arr);

    int *tmp = (int*) calloc(10, sizeof(int));
    memcpy(tmp, arr, 5*sizeof(int));
    free(arr);
    arr = tmp;

    //arr = (int*) realloc(arr, 100000*sizeof(int));

    printf("%p - %i\n", arr, *arr);

    
    
    return 0;
}

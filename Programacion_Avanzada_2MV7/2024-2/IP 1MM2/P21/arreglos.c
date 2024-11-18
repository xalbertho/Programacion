/**
 * @file arreglos.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-19
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int *arr[3];
    arr[0] = (int *)malloc(3*sizeof(int));
    arr[1] = (int *)malloc(3*sizeof(int));
    arr[2] = (int *)malloc(3*sizeof(int));

    int (*m)[3];
    m = malloc(9*sizeof(int));

    printf("%p - %p - %p\n", m, m+1, m+2);
    
    return 0;
}

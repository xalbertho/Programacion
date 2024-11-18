/**
 * @file main2.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-18
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int *m[3];

    *m = (int *)malloc(3*sizeof(int));
    *(m+1) = (int *)malloc(3*sizeof(int));
    *(m+2) = (int *)malloc(3*sizeof(int));

    printf("%p - %p - %p\n", *m, *(m+1), *(m+2));
    
    return 0;
}

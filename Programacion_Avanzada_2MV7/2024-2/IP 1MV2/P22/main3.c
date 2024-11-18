/**
 * @file main3.c
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
    int (*arr)[3];
    arr = (int*)malloc(9*sizeof(int));

    *(*(arr+1)+1) = 10;
    arr+1;
    *arr+1;
    return 0;
}

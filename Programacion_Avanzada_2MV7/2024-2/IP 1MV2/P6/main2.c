/**
 * @file main2.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-02-29
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int arreglo[5];
    arreglo[0] = 1;
    arreglo[500] = 10;

    printf("%i", arreglo[500]);

    return 0;
}

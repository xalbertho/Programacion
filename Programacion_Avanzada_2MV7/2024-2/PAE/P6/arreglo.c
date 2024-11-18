/**
 * @file arreglo.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-03-01
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int arreglo[5];

    arreglo[0] = 10;
    arreglo[500] = 100;

    printf("%i\n", arreglo[500]);

    return 0;
}

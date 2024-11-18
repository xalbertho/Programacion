/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Arreglos
 * @version 0.1
 * @date 2024-03-01
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int arrg[5];
    arrg[0] = 10;
    arrg[500] = 100;

    printf("%i\n", arrg[550]);
    return 0;
}

/**
 * @file main2.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief WHILE
 * @version 0.1
 * @date 2024-02-23
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int variable = 1; // 1.- Variable con valor inicial
    while(variable < 10) // 2.- Condicion
    {
        variable<<=1;// 3.- Una forma de modificar la variable para que eventualmente ya no se cumpla la condicion
        printf("Hola\n");
    }
    return 0;
}

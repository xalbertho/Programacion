/**
 * @file main3.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Do-WHILE
 * @version 0.1
 * @date 2024-02-27
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int variable = -5;// 1. Variable con un valor inicial
    do
    {
        printf("Hola\n");
        variable--; // 3. Una operacion a la variable para que eventualmente la condicion se haga falso
    }while(variable > 0); // 2. Una condicion
    return 0;
}

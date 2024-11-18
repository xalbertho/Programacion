/**
 * @file main3.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief DO-WHILE
 * @version 0.1
 * @date 2024-02-23
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int variable = 10; 
    do
    {
        variable<<=1;
        printf("Hola\n");
    } while(variable < 10);
    return 0;
}

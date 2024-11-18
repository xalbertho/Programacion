/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Mi primer funcion
 * @version 0.1
 * @date 2024-03-20
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>


int suma(int a, int b) {
    return a + b;
}

int main()
{
    int a;
    printf("%i\n", suma(5,8));
    
    return 0;
}

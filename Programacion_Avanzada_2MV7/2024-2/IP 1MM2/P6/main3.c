/**
 * @file main3.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Fibonacci
 * @version 0.1
 * @date 2024-02-28
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int maximo, a = 1, b = 1, c;

    printf("Ingrese la cantidad de digitos que desea: ");
    scanf("%i", &maximo);

    printf("%i %i ", a, b);

    for (int i = 2; i < maximo; i++)
    {
        c=a+b;
        a=b;
        b=c;
        printf("%i ", c);
    }
    
    return 0;
}

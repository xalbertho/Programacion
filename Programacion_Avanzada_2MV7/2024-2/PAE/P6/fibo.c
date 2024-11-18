/**
 * @file fibo.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Imprime la sucesion de Fibonacci.
 * @version 0.1
 * @date 2024-03-01
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int a = 1, b = 1, c, p, i;

    printf("Querido usuario, ingrese la cantidad de terminos de la sucesion (mayor a 2): ");
    scanf("%i", &p);

    printf("%i %d ", a, b);
    
    for (i = 2;i < p;i++)
    {
        c = a + b;
        printf("%i ", c);
        a = b;
        b = c;
        
    }
    
    return 0;
}

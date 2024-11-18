/**
 * @file main2.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Factorial
 * @version 0.1
 * @date 2024-02-28
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int numero;
    unsigned long long factorial =1;
    printf("Usuario, ingrese un numero: ");
    scanf("%d", &numero);
    for (int i = numero; i > 0; i--)
    {
        factorial = factorial *i;
    }

    printf("El factorial de %d es %llu\n", numero, factorial);
    
    return 0;
}

/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-03-12
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

/**
 * @brief Suma dos enteros
 * 
 * @param a Primer entero
 * @param b Segundo entero
 * @return int La suma de a y b
 */
int suma(int a, int b);

int main()
{
    printf("%i\n", suma(7,8));

    return 1;
}

int suma(int a, int b) {
    int sum;
    sum = a + b;
    return sum;
}

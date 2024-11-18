/**
 * @file funciones.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Funciones
 * @version 0.1
 * @date 2024-03-07
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>

/**
 * @brief Funcion que suma dos enteros.
 * 
 * @param a Primer entero
 * @param b Segundo entero
 * @return int La suma de a y b
 */
int suma(int a, int b);

int main()
{
    int va = 5, vb = 6;
    int c = suma(va, vb);
    printf("%i", c);
    return 0;
}

int suma(int a, int b)
{
    int c;
    c = a + b;
    return c;
}

/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Ejemplo de recursion
 * @version 0.1
 * @date 2024-03-21
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>

int factorial(int n)
{
    if (n == 0)
        return 1;
    else
        return n *factorial(n - 1);
}

int main()
{
    printf("%i\n", factorial(5));

    return 0;
}

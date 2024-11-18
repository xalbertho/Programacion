/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-02-29
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>

int main()
{
    int a = 1, b = 1, c, n, i = 2;

    printf("Usuario, ingresa la cantidad de numeros que desee ver de la sucesion de Fibonnaci (mayor a 2): ");
    scanf("%i", &n);

    printf("%i %d ", a, b);

    for (i = 2; i < n;)
    {
        i++;
        c = a + b;
        a = b;
        b = c;
        printf("%i ", c);
    }
    return 0;
}

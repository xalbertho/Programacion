/**
 * @file main4.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-02-22
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>

int main()
{
    int var = 100; // Condicion inicial
    do
    {
        var <<= 1; // Modificacion para que se detenga eventualmente
        printf("Hola\n");
    } while (var < 10); // Condicion final (cuando se va a detener)

    return 0;
}

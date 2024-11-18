/**
 * @file main2.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Uso de funciones de entrada y salida 2
 * @version 0.1
 * @date 2024-02-16
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    char cadena[5];

    fgets(cadena,5, stdin);
    puts(cadena);

    return 0;
}

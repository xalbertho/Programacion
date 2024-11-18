/**
 * @file main2.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Manejo de entradas y salidas
 * @version 0.1
 * @date 2024-02-19
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    char letras[5];

    fgets(letras, 5, stdin);

    puts(letras);

    return 0;
}

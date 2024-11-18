/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Uso de funciones de entrada y salida
 * @version 0.1
 * @date 2024-02-16
 * 
 */
#include<stdio.h>

int main()
{
    char entrada;
    entrada = getc(stdin);
    putc(entrada, stdout);

    entrada = getc(stdin);
    putc(entrada, stdout); 
    return 0;
}

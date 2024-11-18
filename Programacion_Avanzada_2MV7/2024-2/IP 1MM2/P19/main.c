/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-12
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main()
{
    char cadena[100];
    printf("Usuario, ingrese una cadena: ");
    fgets(cadena, 100, stdin);

    for (int i = strlen(cadena) - 1; i >= 0; i--)
    {
        putc(cadena[i], stdout);
    }

    return 0;
}

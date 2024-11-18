/**
 * @file contador.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-03-27
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>
#include"funciones.h"

int main()
{
    int maximo;
    printf("Usuario, ingresa un numero entero positivo: ");
    scanf("%i", &maximo);

    cuenta2(maximo);
    
    return 0;
}

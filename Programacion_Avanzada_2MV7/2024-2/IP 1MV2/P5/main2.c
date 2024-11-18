/**
 * @file main2.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-02-26
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int numero, suma = 0;

    printf("Usuario, ingresa un numero entero positivo: ");
    scanf("%d", &numero);

    while (numero > 0)
    {
        suma += (numero % 10);
        numero /= 10;
    }

    printf("La suma de los digitos es %d\n", suma);
    
    
    return 0;
}

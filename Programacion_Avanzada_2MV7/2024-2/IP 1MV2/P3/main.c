/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-02-20
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>
#define CONSTANTE 56

int global; // NO SE DEBEN USAR

int main()
{
    const int local=6;

    {
        static int local2;
        printf("6", local);
    }

    printf("%s", ((local != 6? "Si es 6": "No es 6")));

    printf("Hola");
    printf("Hola");
    printf("Hola");
    printf("Hola");
    printf("Hola");
    
    return 0;
}

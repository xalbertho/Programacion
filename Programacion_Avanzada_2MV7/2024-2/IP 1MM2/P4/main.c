/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Variables y constantes
 * @version 0.1
 * @date 2024-02-21
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>
#define PI 3

int global; // NO SE DEBE DE USAR

int main()
{
    const int CONSTANTE = 7;
    int VARCONSTANTE;


    static int local = PI;

    {
        int local2;
    }

    //printf("", local2);

    printf("%s", (local != 3? "Es igual a 3" : "No es 3"));


    return 0;
}

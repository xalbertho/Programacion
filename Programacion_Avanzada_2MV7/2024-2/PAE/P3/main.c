/**
 * main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Variable y constantes
 * @date 2024-02-21
*/
#include<stdio.h>
#define PI 3
#define PRINT printf("Hola a todes");



int global; // NO USAR, 0 

int main() 
{
    const int CONSTANTE = 8;



    int local = PI;
    //PI = 5;

    {
        static int local2;
        local = 6;
    }

    //local2 = 9;

    printf("%s", (local != 5? "Es igual a 5": "No es igual a 5"));


}
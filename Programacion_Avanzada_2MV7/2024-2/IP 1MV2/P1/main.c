/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Este es mi primer programa
 * @version 0.1
 * @date 2024-02-15
 * 
 */
#include<stdio.h>

int main()
{
    char caracter[5];
    
    fgets(caracter, 5, stdin);

    puts(caracter);
    return 0;
}

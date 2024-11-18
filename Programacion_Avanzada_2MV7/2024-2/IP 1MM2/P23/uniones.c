/**
 * @file uniones.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-30
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

typedef struct Estructura
{
    char caracter;
    int entero;
    float flotante;
    double doble;
} Estructura;

typedef union Union
{
    char caracter;
    int entero;
    float flotante;
    double doble;
} Union;

int main()
{
    Estructura var1;
    var1.caracter = 'a';
    var1.doble = 1.2;
    var1.entero = 45;
    var1.flotante = 7.6f;
    
    printf("%lu\n", sizeof(Estructura));
    printf("%c - %f - %i - %f\n", var1.caracter, var1.doble, var1.entero, var1.flotante);
    

    Union unionn;
    //unionn.caracter = 'a';
    //unionn.doble = 1.2;
    //unionn.entero = 45;
    unionn.flotante = 7.6f;

    printf("%lu\n", sizeof(Union));
    printf("%c - %f - %i - %f\n", unionn.caracter, unionn.doble, unionn.entero, unionn.flotante);
    
    return 0;
}


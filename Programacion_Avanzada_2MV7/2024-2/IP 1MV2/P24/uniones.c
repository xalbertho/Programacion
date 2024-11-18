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
    var1.caracter = 'z';
    var1.entero = 10;
    var1.flotante = 4.5f;
    var1.doble = 5.6;

    printf("%lu\n%c - %i - %f - %lf\n", sizeof(Estructura), var1.caracter, var1.entero, var1.flotante, var1.doble);
    printf("%p - %p - %p - %p - %p\n", &var1, &var1.caracter, &var1.entero, &var1.flotante, &var1.doble);

    Union var2;
    var2.caracter = 'z';
    var2.entero = 10;
    var2.flotante = 4.5f;
    var2.doble = 5.6;

    printf("%lu\n%c - %i - %f - %lf\n", sizeof(Union), var2.caracter, var2.entero, var2.flotante, var2.doble);

    
    return 0;
}

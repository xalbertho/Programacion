/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Ejemplo de funciones
 * @version 0.1
 * @date 2024-03-19
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>
#include"maizoro.h"
#include"maizoro.h"
#include"maizoro.h"
#include"maizoro.h"


int main()
{
    float valor1, valor2, suma, resta, multi, divi;
    printf("Usuario, ingrese un numero: ");
    scanf("%f", &valor1);
    printf("Usuario, ingrese otro numero: ");
    scanf("%f", &valor2);

    maizoro(valor1, valor2, &suma, &resta, &multi, &divi);


    printf("Suma: %f\nResta: %f\nMultiplicacion: %f\nDivision: %f\n",suma, resta, multi, divi);
    
    
    return 0;
}


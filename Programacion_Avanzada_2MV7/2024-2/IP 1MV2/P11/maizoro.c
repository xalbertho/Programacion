/**
 * @file maizoro.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Calculadora basica
 * @version 0.1
 * @date 2024-03-19
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include "fmaizoro.h"



int main()
{
    float valor1, valor2, res, suma, resta, mult, divi;
    printf("Usuario, ingrese un valor: ");
    scanf("%f", &valor1);

    printf("Usuario, ingrese otro valor: ");
    scanf("%f", &valor2);

    maizoro(valor1, valor2, &suma, &resta, &mult, &divi);

    printf("Suma: %f\nResta: %f\nMultiplicacion: %f\nDivision: %f\n", suma, resta, mult, divi);

    return 0;
}


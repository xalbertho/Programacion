/**
 * @file promedio.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Programa que calcula el promedio de 5 numeros
 * @version 0.1
 * @date 2024-02-23
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>

int main()
{
    int numero, n;
    int suma = 0;
    float promedio;

    printf("Cuantos numeros quieres promediar? ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        printf("Dato %i: ", i+1);
        scanf("%i", &numero);
        suma += numero;
    }

    promedio = (float)suma / (float)n;

    printf("El promedio es: %.2f\n", promedio);

    return 0;
}

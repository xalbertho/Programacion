/**
 * @file promedio.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Programa que solicita al usuario 5 valores e imprime su promedio.
 * @version 0.1
 * @date 2024-02-27
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>

int main()
{
    int var1;
    int suma = 0;
    float promedio;
    int n;

    printf("Usuario, cuantos datos quieres promediar? ");
    scanf("%d", &n);

    if (n < 1)
    {
        printf("No seas tonto, ese valor no existe\n");
    }
    else
    {
        for (int i = 0; i < n; i++)
        {
            printf("Ingrese valor %i: ", i + 1);
            scanf("%i", &var1);
            suma += var1;
        }

        promedio = (float)suma / (float)n;

        printf("El promedio es: %.2f\n", promedio);
    }

    return 0;
}

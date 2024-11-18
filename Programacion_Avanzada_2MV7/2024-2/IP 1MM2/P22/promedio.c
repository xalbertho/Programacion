/**
 * @file promedio.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-23
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>

int main()
{
    char cadena[100];
    double *arr = NULL;
    int count = 0;
    double suma = 0, prom;

    do
    {
        printf("Usuario, ingrese un dato o punto (.) para finalizar: ");
        fgets(cadena, 100, stdin);

        if (cadena[0] != '.')
        {
            if (arr == NULL)
            {
                arr = (double *)malloc(sizeof(double));
                *arr = atof(cadena);
                count++;
            }
            else
            {
                arr = (double *)realloc(arr, (count + 1) * sizeof(double));
                *(arr + count) = atof(cadena);
                count++;
            }
        }
    } while (cadena[0] != '.');

    for (int i = 0; i < count; i++)
    {
        printf("%lf ", *(arr + i));
        suma += *(arr + i);
    }

    prom = suma / (double)count;

    printf("\nPromedio: %lf\n", prom);

    free(arr);

    return 0;
}

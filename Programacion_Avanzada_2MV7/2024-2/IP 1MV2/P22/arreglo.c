/**
 * @file arreglo.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-18
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>

int main()
{
    char valor[100];
    double *valores, temp, suma = 0.0, prom;
    int n = 0;
    do
    {
        printf("Ingrese un valor o f si ya terminaste: ");
        fgets(valor, 100, stdin);
        if (valor[0] != 'f' || valor[0] != 'F')
        {
            temp = atof(valor);
            if (n == 0)
            {
                valores = (double *)malloc(sizeof(double));
                *valores = temp;
            }
            else
            {
                valores = (double *)realloc(valores, (n + 1) * sizeof(double));
                *(valores + n) = temp;
            }
            n++;
        }
    } while (valor[0] != 'f' && valor[0] != 'F');

    n--;
    for (int i = 0; i < n; i++)
    {
        suma += valores[i];
        printf("%lf ", valores[i]);
    }
    printf("\nPromedio %lf\n", suma / (double)(n));

    return 0;
}

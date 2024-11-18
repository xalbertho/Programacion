/**
 * @file main2.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-03-05
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int n, suma = 0;
    float promedio;

    printf("Usuario, ingrese la cantidad de numeros a promediar: ");
    scanf("%i", &n);

    if(n < 1) {
        printf("A caso eres tonto? >:|");
        return 0;
    }

    int arr[n];

    for (int i = 0; i < n; i++)
    {
        printf("Ingrese el valor %i: ", i+1);
        scanf("%i", &arr[i]);
    }

    for (int i = 0; i < n; i++)
    {
        suma+=arr[i];
    }

    promedio = (float)suma / (float)n;
    
    printf("El promedio es: %.2f", promedio);
    
    return 0;
}

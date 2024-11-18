/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-02-26
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int var1, veces;
    int suma = 0;
    float promedio;

    printf("Usuario, ingresa la cantidad de valores que necesitas: ");
    scanf("%d", &veces);

    for (int i = 1; i <= veces; i++)
    {
        printf("Dame el valor %d: ", i);
        scanf("%i", &var1);
        suma = suma + var1;
    }
    
    promedio = (float)suma / (float)veces;

    printf("El promedio es: %.2f\n", promedio);

    return 0;
}

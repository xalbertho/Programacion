/**
 * @file main3.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Ejemplo de matrices
 * @version 0.1
 * @date 2024-03-05
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int matrix[2][3], cont = 1, escalar;

    for (int fila = 0; fila < 2; fila++)
    {
        for (int columna = 0; columna < 3; columna++)
        {
            matrix[fila][columna] = cont++;
        }
    }

    printf("Usuario, ingrese el escalar a sumar: ");
    scanf("%i", &escalar);

    for (int fila = 0; fila < 2; fila++)
    {
        for (int columna = 0; columna < 3; columna++)
        {
            matrix[fila][columna] += escalar;
        }
    }

    for (int fila = 0; fila < 2; fila++)
    {
        for (int columna = 0; columna < 3; columna++)
        {
            printf("%i ", matrix[fila][columna]);
        }
        printf("\n");
    }
    
    
    return 0;
}

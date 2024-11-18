/**
 * @file matriz.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-03-06
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int matrix[3][3],cont=1;

    for (int f = 0; f < 3; f++)
    {
        for (int c = 0; c < 3; c++)
        {
            matrix[f][c] = cont++;
        }
    }
    
    for (int fila = 0; fila < 3; fila++)
    {
        for (int columna = 0; columna < 3; columna++)
        {
            printf("%10i ", matrix[fila][columna]);   
        }
        printf("\n");
    }
    
    
    return 0;
}

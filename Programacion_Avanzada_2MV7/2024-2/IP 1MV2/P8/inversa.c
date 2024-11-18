/**
 * @file inversa.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Programa que permite calcular la inversa de una matriz de 3x3
 * @version 0.1
 * @date 2024-03-05
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>

int main()
{
    int matrix[3][3] = {{1, 2, -3}, {4, 5, 6}, {7, 8, 9}};
    int determinante;
    int matrixT[3][3], matrixAdj[3][3];
    float factor, matrixInv[3][3];

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%i ", matrix[i][j]);
        }
        printf("\n");
    }

    printf("\n");

    // Determinante
    determinante = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]);
    if (determinante == 0)
    {
        printf("No tiene inversa :'c\n");
        return 1;
    }
    factor = 1.0f / (float)determinante;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            matrixT[j][i] = matrix[i][j];
        }
    }

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%i ", matrixT[i][j]);
        }
        printf("\n");
    }

    printf("\n");

    // Adjunta
    matrixAdj[0][0] = (matrixT[1][1] * matrixT[2][2] - matrixT[1][2] * matrixT[2][1]);
    matrixAdj[0][1] = -(matrixT[1][0] * matrixT[2][2] - matrixT[1][2] * matrixT[2][0]);
    matrixAdj[0][2] = (matrixT[1][0] * matrixT[2][1] - matrixT[1][1] * matrixT[2][0]);
    matrixAdj[1][0] = -(matrixT[0][1] * matrixT[2][2] - matrixT[0][2] * matrixT[2][1]);
    matrixAdj[1][1] = (matrixT[0][0] * matrixT[2][2] - matrixT[0][2] * matrixT[2][0]);
    matrixAdj[1][2] = -(matrixT[0][0] * matrixT[2][1] - matrixT[0][1] * matrixT[2][0]);
    matrixAdj[2][0] = (matrixT[0][1] * matrixT[1][2] - matrixT[0][2] * matrixT[1][1]);
    matrixAdj[2][1] = -(matrixT[0][0] * matrixT[1][2] - matrixT[0][2] * matrixT[1][0]);
    matrixAdj[2][2] = (matrixT[0][0] * matrixT[1][1] - matrixT[0][1] * matrixT[1][0]);

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%i ", matrixAdj[i][j]);
        }
        printf("\n");
    }

    printf("\n");

    for (int f = 0; f < 3; f++)
    {
        for (int c = 0; c < 3; c++)
        {
            matrixInv[f][c] = factor * (float)matrixAdj[f][c];
        }
    }
    
    
    
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%5.2f ", matrixInv[i][j]);
        }
        printf("\n");
    }


    return 0;
}

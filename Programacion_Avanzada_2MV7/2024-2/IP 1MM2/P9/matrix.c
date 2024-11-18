/**
 * @file matrix.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Ejemplos de matrices
 * @version 0.1
 * @date 2024-03-06
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>

int main()
{
    int matrix[3][3]={{1,2,3},{4,4,6},{7,8,9}}, matrixTrans[3][3], matrixA[3][3], cont = 1, determinante;
    float matrixI[3][3];
    float factor;


    // Determinante
    determinante = (matrix[0][0] * matrix[1][1] * matrix[2][2]) +
                   (matrix[0][1] * matrix[1][2] * matrix[2][0]) +
                   (matrix[0][2] * matrix[1][0] * matrix[2][1]) -
                   (matrix[2][0] * matrix[1][1] * matrix[0][2]) -
                   (matrix[2][1] * matrix[1][2] * matrix[0][0]) -
                   (matrix[2][2] * matrix[1][0] * matrix[0][1]);

    if (determinante == 0)
    {
        printf("Lo siento, esa matriz no tiene inversa :'(\n");
        return 1;
    }

    factor = 1.0f / (float)determinante;

    // Traspuesta
    for (int f = 0; f < 3; f++)
    {
        for (int c = 0; c < 3; c++)
        {
            matrixTrans[c][f] = matrix[f][c];
        }
    }

    // Adjunta
    matrixA[0][0] = +1 * ((matrixTrans[1][1] * matrixTrans[2][2] - matrixTrans[1][2] * matrixTrans[2][1]));
    matrixA[0][1] = -1 * ((matrixTrans[1][0] * matrixTrans[2][2] - matrixTrans[2][0] * matrixTrans[1][2]));
    matrixA[0][2] = +1 * ((matrixTrans[1][0] * matrixTrans[2][1] - matrixTrans[2][0] * matrixTrans[1][1]));
    matrixA[1][0] = -1 * ((matrixTrans[0][1] * matrixTrans[2][2] - matrixTrans[0][2] * matrixTrans[2][1]));
    matrixA[1][1] = +1 * ((matrixTrans[0][0] * matrixTrans[2][2] - matrixTrans[0][2] * matrixTrans[2][0]));
    matrixA[1][2] = -1 * ((matrixTrans[0][0] * matrixTrans[2][1] - matrixTrans[0][1] * matrixTrans[2][0]));
    matrixA[2][0] = +1 * ((matrixTrans[0][1] * matrixTrans[1][2] - matrixTrans[0][2] * matrixTrans[1][1]));
    matrixA[2][1] = -1 * ((matrixTrans[0][0] * matrixTrans[1][2] - matrixTrans[1][0] * matrixTrans[0][2]));
    matrixA[2][2] = +1 * ((matrixTrans[0][0] * matrixTrans[1][1] - matrixTrans[0][1] * matrixTrans[1][0]));

    for (int f = 0; f < 3; f++)
    {
        for (int c = 0; c < 3; c++)
        {
            matrixI[f][c] = (float)matrixA[f][c] * factor;
        }
    }


    for (int fila = 0; fila < 3; fila++)
    {
        for (int columna = 0; columna < 3; columna++)
        {
            printf("%6.3f ", matrixI[fila][columna]);
        }
        printf("\n");
    }

    
    return 0;
}

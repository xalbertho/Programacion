/**
 * @file inversa.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-03-11
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>

int main()
{
    int matrix[3][3] = {{1, 2, 3}, {4, 5, 5}, {7, 8, 9}};
    int matrixT[3][3], matrixA[3][3], determinante;
    float factor, matrixI[3][3];

    // Determinante
    determinante = (matrix[0][0] * matrix[1][1] * matrix[2][2]) + (matrix[0][1] * matrix[1][2] * matrix[2][0]) + (matrix[0][2] * matrix[1][0] * matrix[2][1]) - (matrix[0][2] * matrix[1][1] * matrix[2][0]) - (matrix[0][0] * matrix[1][2] * matrix[2][1]) - (matrix[0][1] * matrix[1][0] * matrix[2][2]);

    if(determinante == 0) {
        printf("Upss, la matriz no tiene inversa :'(\n");
        return 0;
    }

    factor = 1.0f / (float)determinante;

    // Traspuesta
    for (int f = 0; f < 3; f++)
    {
        for (int c = 0; c < 3; c++)
        {
            matrixT[c][f] = matrix[f][c];
        }
    }

    // Adjunta
    matrixA[0][0] = +1 * (matrixT[1][1]*matrixT[2][2]-matrixT[1][2]*matrixT[2][1]);
    matrixA[0][1] = -1 * (matrixT[1][0]*matrixT[2][2]-matrixT[1][2]*matrixT[2][0]);
    matrixA[0][2] = +1 * (matrixT[1][0]*matrixT[2][1]-matrixT[2][0]*matrixT[1][1]);
    matrixA[1][0] = -1 * (matrixT[0][1]*matrixT[2][2]-matrixT[0][2]*matrixT[2][1]);
    matrixA[1][1] = +1 * (matrixT[0][0]*matrixT[2][2]-matrixT[0][2]*matrixT[2][0]);
    matrixA[1][2] = -1 * (matrixT[0][0]*matrixT[2][1]-matrixT[0][1]*matrixT[2][0]);
    matrixA[2][0] = +1 * (matrixT[0][1]*matrixT[1][2]-matrixT[0][2]*matrixT[1][1]);
    matrixA[2][1] = -1 * (matrixT[0][0]*matrixT[1][2]-matrixT[0][2]*matrixT[1][0]);
    matrixA[2][2] = +1 * (matrixT[0][0]*matrixT[1][1]-matrixT[0][1]*matrixT[1][0]);


    // Multiplicacion por factor
    for (int f = 0; f < 3; f++)
    {
        for (int c = 0; c < 3; c++)
        {
            matrixI[f][c] = factor * (float)matrixA[f][c];
        }
    }

    //Imprimimos


    for (int f = 0; f < 3; f++)
    {
        for (int c = 0; c < 3; c++)
        {
            printf("%i ", matrix[f][c]);
        }
        printf("\n");
    }

    printf("\n");
    for (int f = 0; f < 3; f++)
    {
        for (int c = 0; c < 3; c++)
        {
            printf("%5.2f ", matrixI[f][c]);
        }
        printf("\n");
    }

    return 0;
}

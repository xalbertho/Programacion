/**
 * @file inversa.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-03-11
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <iostream>

using namespace std;

int main()
{
    int matrix[3][3] = {{1, 2, 3}, {4, 5, 6}, {6, 8, 9}};
    int matrixT[3][3], matrixA[3][3];
    int determinante;
    float factor, matrixI[3][3];

    // Determinante
    determinante = matrix[0][0] * matrix[1][1] * matrix[2][2] +
                   matrix[0][1] * matrix[1][2] * matrix[2][0] +
                   matrix[0][2] * matrix[1][0] * matrix[2][1] -
                   matrix[2][0] * matrix[1][1] * matrix[0][2] -
                   matrix[2][1] * matrix[1][2] * matrix[0][0] -
                   matrix[2][2] * matrix[1][0] * matrix[0][1];

    if (determinante == 0)
    {
        cout << "Upss, no tiene inversa :'(" << endl;
        return 1;
    }

    factor = 1.0f / (float)determinante;

    // Traspuesta

    for (int f = 0; f < 3; f++)
    {
        for (int c = 0; c < 3; c++)
        {
            matrixT[f][c] = matrix[c][f];
        }
    }

    // Adjunta
    matrixA[0][0] = +1 * (matrixT[1][1] * matrixT[2][2] - matrixT[2][1] * matrixT[1][2]);
    matrixA[0][1] = -1 * (matrixT[1][0] * matrixT[2][2] - matrixT[1][2] * matrixT[2][0]);
    matrixA[0][2] = +1 * (matrixT[1][0] * matrixT[2][1] - matrixT[2][0] * matrixT[1][1]);
    matrixA[1][0] = -1 * (matrixT[0][1] * matrixT[2][2] - matrixT[0][2] * matrixT[2][1]);
    matrixA[1][1] = +1 * (matrixT[0][0] * matrixT[2][2] - matrixT[0][2] * matrixT[2][0]);
    matrixA[1][2] = -1 * (matrixT[0][0] * matrixT[2][1] - matrixT[0][1] * matrixT[2][0]);
    matrixA[2][0] = +1 * (matrixT[0][1] * matrixT[1][2] - matrixT[1][1] * matrixT[0][2]);
    matrixA[2][1] = -1 * (matrixT[0][0] * matrixT[1][2] - matrixT[0][2] * matrixT[1][0]);
    matrixA[2][2] = +1 * (matrixT[0][0] * matrixT[1][1] - matrixT[0][1] * matrixT[1][0]);

    // Multiplicamos
    for (int f = 0; f < 3; f++)
    {
        for (int c = 0; c < 3; c++)
        {
            matrixI[f][c] = factor * (float)matrixA[f][c];
        }
    }

    for (int f = 0; f < 3; f++)
    {
        for (int c = 0; c < 3; c++)
        {
            cout << matrixI[f][c] << " ";
        }
        cout << endl;
    }

    cout << endl;

    return 0;
}

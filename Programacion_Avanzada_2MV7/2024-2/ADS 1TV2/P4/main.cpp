/**
 * @file main.cpp
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
    int matrix[3][3] = {{1,2,3},{4,6,6},{7,8,9}};
    int matrixT[3][3], matrixA[3][3], determinate, cont = 0;
    float factor, matrixI[3][3];


    // Determinante
    determinate = matrix[0][0] * matrix[1][1] * matrix[2][2] +
                  matrix[1][0] * matrix[2][1] * matrix[0][2] +
                  matrix[2][0] * matrix[0][1] * matrix[1][2] -
                  matrix[2][0] * matrix[1][1] * matrix[0][2] -
                  matrix[0][0] * matrix[2][1] * matrix[1][2] -
                  matrix[1][0] * matrix[0][1] * matrix[2][2];

    if(determinate == 0) {
        cout << "Lo siento, la matriz no tiene inversa :'("<< endl;
        return 1;
    }

    factor = 1.0f/(float)determinate;

    // Transponer
    for (int fila = 0; fila < 3; fila++)
    {
        for (int columna = 0; columna < 3; columna++)
        {
            matrixT[columna][fila] = matrix[fila][columna];
        }
    }

    // Adjunta
    matrixA[0][0] = +1 * ((matrixT[1][1] * matrixT[2][2]) - (matrixT[2][1] * matrixT[1][2]));
    matrixA[0][1] = -1 * ((matrixT[1][0] * matrixT[2][2]) - (matrixT[1][2] * matrixT[2][0]));
    matrixA[0][2] = +1 * ((matrixT[1][0] * matrixT[2][1]) - (matrixT[1][1] * matrixT[2][0]));
    matrixA[1][0] = -1 * ((matrixT[0][1] * matrixT[2][2]) - (matrixT[0][2] * matrixT[2][1]));
    matrixA[1][1] = +1 * ((matrixT[0][0] * matrixT[2][2]) - (matrixT[2][0] * matrixT[0][2]));
    matrixA[1][2] = -1 * ((matrixT[0][0] * matrixT[2][1]) - (matrixT[0][1] * matrixT[2][0]));
    matrixA[2][0] = +1 * ((matrixT[0][1] * matrixT[1][2]) - (matrixT[1][1] * matrixT[0][2]));
    matrixA[2][1] = -1 * ((matrixT[0][0] * matrixT[1][2]) - (matrixT[1][0] * matrixT[0][2]));
    matrixA[2][2] = +1 * ((matrixT[0][0] * matrixT[1][1]) - (matrixT[1][0] * matrixT[0][1]));


    for (int fila = 0; fila < 3; fila++)
    {
        for (int columna = 0; columna < 3; columna++)
        {
            matrixI[fila][columna] = factor * (float)matrixA[fila][columna];
        }
    }

    
    
    for (int fila = 0; fila < 3; fila++)
    {
        for (int columna = 0; columna < 3; columna++)
        {
            cout << matrixI[fila][columna] << " ";
        }
        cout << endl;
    }

    return 0;
}

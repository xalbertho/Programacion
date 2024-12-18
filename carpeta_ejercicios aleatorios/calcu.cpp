#include <iostream>

// Funci�n para ingresar una matriz desde el usuario
void ingresarMatriz(int matriz[][10], int filas, int columnas, const std::string& nombre) {
    std::cout << "Ingrese los elementos de la matriz " << nombre << " (" << filas << "x" << columnas << "):\n";
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            std::cout << nombre << "[" << i+1 << "][" << j+1 << "]: ";
            std::cin >> matriz[i][j];
        }
    }
}

// Funci�n para mostrar una matriz
void mostrarMatriz(int matriz[][10], int filas, int columnas) {
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            std::cout << matriz[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

// Funci�n para realizar la suma de dos matrices
void sumaMatrices(int matrizA[][10], int matrizB[][10], int resultado[][10], int filas, int columnas) {
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            resultado[i][j] = matrizA[i][j] + matrizB[i][j];
        }
    }
}

// Funci�n para realizar la resta de dos matrices
void restaMatrices(int matrizA[][10], int matrizB[][10], int resultado[][10], int filas, int columnas) {
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            resultado[i][j] = matrizA[i][j] - matrizB[i][j];
        }
    }
}

// Funci�n para realizar la multiplicaci�n de dos matrices
void multiplicarMatrices(int matrizA[][10], int matrizB[][10], int resultado[][10], int filasA, int columnasA, int columnasB) {
    for (int i = 0; i < filasA; i++) {
        for (int j = 0; j < columnasB; j++) {
            resultado[i][j] = 0;
            for (int k = 0; k < columnasA; k++) {
                resultado[i][j] += matrizA[i][k] * matrizB[k][j];
            }
        }
    }
}

// Funci�n para calcular la transposici�n de una matriz
void matrizTranspuesta(int matriz[][10], int transpuesta[][10], int filas, int columnas) {
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            transpuesta[j][i] = matriz[i][j];
        }
    }
}

int main() {
    int matrizA[10][10], matrizB[10][10], resultado[10][10], transpuestaA[10][10], transpuestaB[10][10];
    int filas, columnas,opcion;

    std::cout << "Ingrese el n�mero de filas y columnas para las matrices: ";
    std::cin >> filas >> columnas;

    ingresarMatriz(matrizA, filas, columnas, "A");
    ingresarMatriz(matrizB, filas, columnas, "B");

    std::cout << "Seleccione la operaci�n a realizar:\n";
    std::cout << "1. Suma\n";
    std::cout << "2. Resta\n";
    std::cout << "3. Multiplicaci�n\n";
    std::cout << "4. Transposici�n (Matriz A)\n";
    std::cout << "5. Transposici�n (Matriz B)\n";
    std::cout << "Ingrese la opci�n: ";
    std::cin >> opcion;

    switch (opcion) {
        case 1:
            sumaMatrices(matrizA, matrizB, resultado, filas, columnas);
            std::cout << "Resultado de la suma:\n";
            mostrarMatriz(resultado, filas, columnas);
            break;
        case 2:
            restaMatrices(matrizA, matrizB, resultado, filas, columnas);
            std::cout << "Resultado de la resta:\n";
            mostrarMatriz(resultado, filas, columnas);
            break;
        case 3:
            multiplicarMatrices(matrizA, matrizB, resultado, filas, columnas, columnas);
            std::cout << "Resultado de la multiplicaci�n:\n";
            mostrarMatriz(resultado, filas, columnas);
            break;
        case 4:
            matrizTranspuesta(matrizA, transpuestaA, filas, columnas);
            std::cout << "Transposici�n de la Matriz A:\n";
            mostrarMatriz(transpuestaA, columnas, filas);
            break;
        case 5:
            matrizTranspuesta(matrizB, transpuestaB, filas, columnas);
            std::cout << "Transposici�n de la Matriz B:\n";
            mostrarMatriz(transpuestaB, columnas, filas);
            break;
        default:
            std::cout << "Opci�n no v�lida.\n";
            break;
    }

    return 0;
}


/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-09
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <iostream>
#include <cstdlib>
#include <ctime>
#define N 10

using namespace std;

void imprime(int *arr, int n)
{
    cout << "\n[ ";
    for (int i = 0; i < n; i++)
    {
        cout << *(arr + i) << " ";
    }
    cout << "]\n";
}

void burbuja(int *arr, int n)
{
    int aux;
    for (int j = 0; j < n - 1; j++)
    {
        for (int i = 0; i < n - 1 - j; i++)
        {
            if (*(arr + i) > *(arr + i + 1))
            {
                aux = *(arr + i);
                *(arr + i) = *(arr + i + 1);
                *(arr + i + 1) = aux;
            }
        }
    }
}

int main()
{
    int arr[N];
    srand(time(NULL));
    for (int i = 0; i < N; i++)
    {
        *(arr + i) = rand() % 101;
    }
    imprime(arr, N);
    burbuja(arr, N);
    imprime(arr, N);

    return 0;
}

/**
 * @file burbuja.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-03-11
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <iostream>
#include <cstdlib>
#include <ctime>
#define N 20

using namespace std;

int main()
{
    int rawr[N];
    srand(time(NULL));

    for (int i = 0; i < N; i++)
    {
        rawr[i] = (rand() % 51) + 50;
    }

    for (int i = 0; i < N; i++)
    {
        cout << rawr[i] << " ";
    }

    cout << endl;
    for (int j = 0; j < N; j++)
    {
        for (int i = 0; i < N - 1 - j; i++)
        {
            if (rawr[i] > rawr[i + 1])
            {
                rawr[i + 1] = rawr[i] + rawr[i + 1];
                rawr[i] = rawr[i + 1] - rawr[i];
                rawr[i + 1] = rawr[i + 1] - rawr[i];
            }
        }
    }

    for (int i = 0; i < N; i++)
    {
        cout << rawr[i] << " ";
    }

    return 0;
}

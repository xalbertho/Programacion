/**
 * @file main.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-11
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<iostream>
#include<cstdlib>
#include<ctime>

using namespace std;

int main()
{
    int arr[3][3];
    int *ptr = *arr;
    srand(time(NULL));

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            *(*(arr + i) + j) = rand()%51;
        }
    }

    for (int i = 0; i < 9; i++)
    {
        cout << *arr + i << " ";
    }
    
    

    return 0;
}

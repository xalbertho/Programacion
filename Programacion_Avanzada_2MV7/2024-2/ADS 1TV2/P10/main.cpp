/**
 * @file main.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-09
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<iostream>

using namespace std;

int main()
{
    int arr[10];
    int *ptr;
    double a;
    double *pa;
    pa = &a;
    arr[0] = 10;

    ptr = arr;

    cout << pa << endl << pa+1;
    return 0;
}

/**
 * @file funciones.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-03-12
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<iostream>

using namespace std;

int suma(int a, int b) {
    return a + b;
}

int main()
{
    int a=5, b=8;
    int c = suma(a,b);

    cout << c;

    return 0;
}

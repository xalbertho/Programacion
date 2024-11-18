/**
 * @file main.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-12
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<iostream>

using namespace std;

void funcion(int *a) {
    *a = 10;
}

void funcion2(int& a) {
    a = 10;
}

int main()
{
    int var=0;

    funcion2(var);

    cout << var;
    
    return 0;
}

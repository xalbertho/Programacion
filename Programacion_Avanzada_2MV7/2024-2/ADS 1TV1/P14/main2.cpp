/**
 * @file main2.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-11
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<iostream>

using namespace std;

void funcion(int *a) {
    *a = 10;
}

void LaFuncion() {
    int *a = new int;
    *a = 0;
}

int main()
{
    while(1) LaFuncion();

    return 0;
    int *var ;
    var = new int;
    *var = 0;

    funcion(var);

    cout << var << endl << *var;
    
    return 0;
}

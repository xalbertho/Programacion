/**
 * @file main.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Sobrecarga de Funciones
 * @version 0.1
 * @date 2024-03-15
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<iostream>

using namespace std;

int suma(int a, int b=9 );
int suma(int a, int b, int c);

float suma(float a, float b);

int main()
{
    cout << suma(4,6);
    return 0;
}

int suma(int a, int b){
    return a + b;
}

int suma(int a, int b, int c) {
    return a+b+c;
}

float suma(float a, float b) {
    return a+b;
}
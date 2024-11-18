/**
 * @file main.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-03-15
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<iostream>

using namespace std;

int suma(int a=5, int b=10);
double suma(double a, double b);
float suma(float a, float b);
double suma(double a, int b);

int suma(int a, int b, int c);

int main()
{
    cout<< suma(3,1);
    
    return 0;
}

int suma(int a, int b) {
    return a + b;
}

double suma(double a, double b) {
    return a + b;
}

double suma(double a, int b){
    return a + (double)b;
}

int suma(int a, int b, int c) {
    return a + b + c;
}
float suma(float a, float b) {
    return a + b;
}

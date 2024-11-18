/**
 * @file recursion.cpp
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

int factorial(int n) {
    if(n==0) return 1;
    return n*factorial(n-1);
}

int main()
{
    
    cout <<factorial(5)<< endl; 
    return 0;
}

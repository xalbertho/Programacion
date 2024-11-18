/**
 * @file main2.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Ejemplo de ramificaciones
 * @version 0.1
 * @date 2024-03-05
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<iostream>

using namespace std;

int main()
{
    int var = 0;// 1. Variable con un valor inicial
    for(;var<10;var++) // 2. Condicion 
    {
        
        cout << var <<endl;
        if((var&1)==1) continue;
         // 3. Mecanismo que modifique la variable para que eventualmente la condicion sea falsa
    }

    return 0;
}

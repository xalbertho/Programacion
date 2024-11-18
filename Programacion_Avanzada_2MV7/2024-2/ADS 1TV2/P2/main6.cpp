/**
 * @file main6.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
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
    for (int i = 0; i < 10; i++)
    {
        if((i&1)==0) continue;
        cout << i << endl;
        
    }
    
    return 0;
}

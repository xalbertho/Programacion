/**
 * @file arreglos.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Arreglos
 * @version 0.1
 * @date 2024-03-07
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<iostream>
#include<vector>
#include<list>

using namespace std;

int main()
{
    int arr[] = {1,2,3,4,5};
    vector<int> vect;
    list<int> lista;

    lista.push_back(1);
    lista.push_back(2);
    lista.push_back(3);
    for(auto e : lista) {
        cout << e << endl;
    }

    return 0;
    vect.push_back(1);
    vect.push_back(2);
    vect.push_back(3);

    for (int i = 0; i < 3; i++)
    {
        cout << vect[i] << endl;
    }
    
    return 0;

    for (int i = 0; i < 5; i++)
    {
        if(i == 2) continue;
        cout << arr[i] << endl;
    }
    
    return 0;
}

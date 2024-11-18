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
    int arrg[2];
    vector<int> arreglo;

    list<int> lista;

    lista.push_back(1);
    lista.push_back(2);
    lista.push_back(3);
    for(auto a : lista) {
        cout << a << endl;
    }

    return 0;

    arreglo.push_back(1);
    arreglo.push_back(2);
    arreglo.push_back(3);

    cout << arreglo[2];

    return 0;


    arrg[0] = 10;
    //arrg[-2] = 100;

    cout << arrg[2] << endl;
    return 0;
}

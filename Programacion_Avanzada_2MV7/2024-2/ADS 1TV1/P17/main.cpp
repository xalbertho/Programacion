/**
 * @file main.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-16
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <iostream>
#include <cstring>
#include<vector>

using namespace std;

template <typename T> class Arreglo
{
private:
    T *ptr;
    int size;

public:
    Arreglo()
    {
        size = 0;
    }

    ~Arreglo()
    {
        delete[] ptr;
    }

    void agregar(T valor)
    {
        if (size == 0)
        {
            ptr = new T[1];
            *ptr = valor;
            size++;
        }
        else
        {
            T *tmp = new T[size + 1];
            memcpy(tmp, ptr, size * sizeof(T));
            *(tmp + size) = valor;
            delete[] ptr;
            ptr = tmp;
            size++;
        }
    }
    int tamanio() { return size; }

    T valueAt(int indice)
    {
        if (indice < 0 || indice >= size)
        {
            throw "Indice fuera de rango.";
        }
        return *(ptr + indice);
    }

    friend ostream &operator<<(ostream &os, Arreglo &arrg)
    {
        os << "[ ";
        for (int i = 0; i < arrg.tamanio(); i++)
        {
            os << arrg.valueAt(i) << " ";
        }
        os << "]";
        return os;
    }
};

template<typename T, typename S> S suma(T a, T b) {
    return (S)(a + b);
}




int main()
{
    suma<int, double>(5,6);
    Arreglo<string> arr;
    arr.agregar("34");

    cout << arr;
    return 0;
}

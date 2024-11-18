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
#include <vector>

using namespace std;

template <typename T>
class Arreglo
{
private:
    T *_arr;
    int cont;

public:
    Arreglo()
    {
        cont = 0;
    }

    ~Arreglo()
    {
        delete[] _arr;
    }

    int tamanio() { return cont; }

    T valoren(int indice)
    {
        if (indice < 0 || indice >= cont)
        {
            throw "Indice fuera de rango";
        }
        return _arr[indice];
    }

    void agregar(T valor)
    {
        if (cont == 0)
        {
            _arr = new T[1];
            *_arr = valor;
            cont++;
        }
        else
        {
            T *tmp = new T[cont + 1];
            memcpy(tmp, _arr, cont * sizeof(T));
            *(tmp + cont) = valor;
            delete[] _arr;
            _arr = tmp;
            cont++;
        }
    }

    friend ostream &operator<<(ostream &os, Arreglo &arr)
    {
        os << "[ ";
        for (int i = 0; i < arr.tamanio(); i++)
        {
            os << arr.valoren(i) << " ";
        }
        os << "]";

        return os;
    }
};

template <typename T, typename S>
S suma(T a, T b)
{
    return (S)(a + b);
}

int main()
{
    Arreglo<string> arr;

    suma<float, double>(5, 7);

    arr.agregar("5.6");

    cout << arr;

    return 0;
}

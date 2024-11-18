/**
 * @file main.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-15
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <iostream>

using namespace std;

class Matrix
{
private:
    int *_m;
    int _filas, _columnas;

public:
    Matrix(int filas, int columnas)
    {
        if (filas < 1 || columnas < 1)
        {
            throw "Dimensiones no validas";
        }
        _filas = filas;
        _columnas = columnas;
        _m = new int[filas * columnas];
    }

    ~Matrix()
    {
        try
        {
            delete[] _m;
        }
        catch(const std::exception& e)
        {
            std::cerr << e.what() << '\n';
        }
        
            
    }

    int getFilas() { return _filas; }
    int getColumnas() { return _columnas; }

    void set(int f, int c, int valor)
    {
        if (f < 0 || f >= _filas)
        {
            throw "Indice de fila incorrecto";
        }
        if (c < 0 || c >= _columnas)
        {
            throw "Indice de columna incorrecto";
        }
        _m[f * _columnas + c] = valor;
    }

    int get(int f, int c)
    {
        if (f < 0 || f >= _filas)
        {
            throw "Indice de fila incorrecto";
        }
        if (c < 0 || c >= _columnas)
        {
            throw "Indice de columna incorrecto";
        }
        return _m[f * _columnas + c];
    }

    friend Matrix operator+(Matrix& m, int escalar)
    {
        Matrix res(m.getFilas(), m.getColumnas());
        for (int i = 0; i < m.getFilas(); i++)
        {
            for (int j = 0; j < m.getColumnas(); j++)
            {
                res.set(i,j, m.get(i,j) + escalar);
            }
            
        }
        return res;
        
    }
};

int main()
{
    int numero;

    try
    {
        Matrix m(3, 3);
        int c = 0;

        for (int i = 0; i < m.getFilas(); i++)
        {
            for (int j = 0; j < m.getColumnas(); j++)
            {
                m.set(i, j, c++);
            }
        }

        Matrix r = m + (-7);

        for (int i = 0; i < m.getFilas(); i++)
        {
            for (int j = 0; j < m.getColumnas(); j++)
            {
                cout << r.get(i, j) << " ";
            }
            cout << endl;
        }
    }
    catch (const char *e)
    {
        std::cerr << e << '\n';
    }
    catch (const int e)
    {
        std::cerr << (e == 1 ? "Tonto" : "Mas tonto") << '\n';
    }
    catch (...)
    {
        std::cerr << "Error generico" << '\n';
    }
    return 0;
}

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
#include<iostream>

using namespace std;

class Matriz {
    private:
    int *m;
    int filas, columnas;

    public:
    Matriz(int filas, int columnas) {
        if(filas < 1 || columnas < 1) {
            throw 1.6;
        }
        this->filas = filas;
        this->columnas = columnas;
        m = new int[filas * columnas];
    }

    ~Matriz() {
        delete[] m;
    }

    int getFilas() { return this->filas;}
    int getColumnas() {return this->columnas;}

    void set(int fila, int columna, int valor) {
        if(fila < 0 || fila >= this->filas) {
            throw "Indice de filas fuera de la dimension de la matriz.";
        }
        if(columna < 0 || columna >= this->columnas) {
            throw "Indice de columnas fuera de la dimension de la matriz.";
        }
        m[fila * this->filas + columna] = valor;
    }

    int get(int fila, int columna) {
        if(fila < 0 || fila >= this->filas) {
            throw "Indice de filas fuera de la dimension de la matriz.";
        }
        if(columna < 0 || columna >= this->columnas) {
            throw "Indice de columnas fuera de la dimension de la matriz.";
        }
        return m[fila * this->filas + columna];
    }


};

Matriz operator+(Matriz& m, int escalar) {
    Matriz res(m.getFilas(), m.getColumnas());
    for (int i = 0; i < m.getFilas(); i++)
    {
        for (int j = 0; j < m.getColumnas(); j++)
        {
            res.set(i,j, m.get(i,j) + escalar);
        } 
    }
    return res;
}

int main()
{
    try
    {
        Matriz m(3,3);
        int cont = 1;

        for (int i = 0; i < m.getFilas(); i++)
        {
            for (int j = 0; j < m.getColumnas(); j++)
            {
                m.set(i,j, cont++);
            }
        }
        //m.set(10,0,100);

        Matriz res = m + 5;

        for (int i = 0; i < m.getFilas(); i++)
        {
            for (int j = 0; j < m.getColumnas(); j++)
            {
                cout << res.get(i,j) << " ";
            }
            cout << endl;
        }
    }
    catch(const char *e)
    {
        std::cerr << "Error: " << e << '\n';
    }
    catch(const int e)
    {
        std::cerr << "Error: " << e << '\n';
    }
    catch(...)
    {
        std::cerr << "Error: Error generico"<< '\n';
    }
    
    

    return 0;
}

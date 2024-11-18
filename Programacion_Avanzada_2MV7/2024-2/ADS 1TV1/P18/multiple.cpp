/**
 * @file multiple.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-19
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<iostream>

using namespace std;

class Papa {
    public:
    string jefe() {
        return "Voy por cigarros, no tardo.";
    }

    string habla() {
        return "No soy la mama";
    }
};

class Mama {
    public:
    string buscar() {
        return "Y si lo encuentro que te hago?";
    }
    string habla() {
        return "Soy la mama";
    }
};

class Hije : public Mama, public Papa {

};

int main()
{
    Hije companiere;
    cout << companiere.buscar();
    cout << companiere.jefe();
    cout << companiere.Mama::habla();
    
    return 0;
}

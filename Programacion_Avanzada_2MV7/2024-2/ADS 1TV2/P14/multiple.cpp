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
    string papear() {
        return "Papeado";
    }
    string hablar() {
        return "Soy el papa";
    }
};

class Mama {
    public:
    string chanclazo() {
        return "Chancleado";
    }
    string hablar() {
        return "Soy la mama";
    }
};

class Hijo : public Mama, public Papa {

};

int main()
{
    Hijo h;
    cout << h.Mama::hablar();
    
    
    return 0;
}

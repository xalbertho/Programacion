/**
 * @file amigos.cpp
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

class Chuchin {
    private:
    string maximo_secreto;
    friend string Alex_de_Meca(Chuchin c);
    friend class Alex;

    public:
    Chuchin() {
        maximo_secreto = "Amo a Alex de Meca";
    }

    string desquite() {
        Alex a;
        return a.maximo_secreto;
    }
};

class Alex {
    private:
    string maximo_secreto;

    public:
    Alex(){
        maximo_secreto = "Amo al crush de Chuchin";
    }

    string chisme() {
        Chuchin c;
        return c.maximo_secreto;
    }
};


string Alex_de_Meca(Chuchin c) {
    return c.maximo_secreto;
}

int main()
{
    Alex a;
    cout << a.chisme();
    
    return 0;
}

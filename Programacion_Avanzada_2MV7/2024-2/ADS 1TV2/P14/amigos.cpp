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
#include <iostream>

using namespace std;


class Yo
{
private:
    string maximo_secreto;
    friend class Amigo;

public:
    Yo()
    {
        maximo_secreto = "Copie la practicas de ADS";
    }

    friend string professor_X(Yo tu);
};

class Amigo {
    private:
    string maximo_secreto;
    public:
    Amigo()
    {
        maximo_secreto = "Me gusta la novia de mi amigo";
    }

    string chisme() {
        Yo yo;
        return yo.maximo_secreto;
    }
};



string professor_X(Yo tu)
{
    return tu.maximo_secreto;
}

int main()
{
    Yo joseluis;
    Amigo leornado;

    cout << leornado.chisme();
    return 0;
}

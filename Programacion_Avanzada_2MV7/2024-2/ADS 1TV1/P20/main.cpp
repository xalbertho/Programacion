/**
 * @file main.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-29
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <iostream>
#include "funciones.hpp"

using namespace std;


int main()
{
    Fecha *fecha = new Fecha(4, 6, 1999);
    cout << fecha->dia();

    /* int entero = 0b00000000000000000000000100001010;
    int8_t *ptr;
    ptr = (int8_t *)&entero;

    //int entero = 0xFFFFFFFF;

    printf("%i\n", *ptr);
    printf("%i\n", *(ptr+1));
    printf("%i\n", *(ptr+2));
    printf("%i\n", *(ptr+3));
 */
    return 0;
}

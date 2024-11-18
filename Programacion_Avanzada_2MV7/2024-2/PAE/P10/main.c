/**
 * @file main.c 
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Ejemplo de paso de parametros
 * @version 0.1
 * @date 2024-03-22
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include "operaciones.h"
#include "tools.h"


int main()
{
    int a = 5, b = 8;
    int seleccion;
    char *opciones[] = {"Sumas", "Restas", "Multiplicaciones", "Divisiones", "Salir"};

    seleccion = showMenu(5, opciones, "La Maizoro");

    printf("%i", seleccion);

    return 0;



    int res = sumaRef(&a, &b);
    //int res = suma(a, b);

    printf("Suma: %i, a: %i b: %i\n", res, a, b);
    return 0;
}


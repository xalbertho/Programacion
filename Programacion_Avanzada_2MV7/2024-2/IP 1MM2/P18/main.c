/**
 * @file main2.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-10
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include "funciones/cadena.h"


int main()
{
    char nombre[200];
    copiar("Jose Luis", nombre);
    concatena(nombre, "\n");
    concatena(nombre, "Hola a ");
    concatena(nombre, "todes");

    printf("%s\n%i", nombre, tamanio(nombre));

    return 0;
}

/**
 * @file sumas.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Cuenta
 * @version 0.1
 * @date 2024-03-22
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include "tools.h"

void cuenta(int maximo, int i)
{
    if (i <= maximo)
    {
        printf("%i ", i);
        i++;
        cuenta(maximo, i);
    }
}

void cuenta2(int maximo)
{
    static int i = 0;
    if (i <= maximo)
    {
        printf("%i ", i);
        i++;
        cuenta2(maximo);
    }
}

int main()
{
    int maximo, sel;
    char *opciones[] = {"Algoritmo 1", "Algoritmo 2", "Salir"};
    do
    {
        sel = showMenu(3, opciones, "Cuentas");

        switch (sel)
        {
        case 0:
            printf("Usuario, ingresa un numero positivo mayor a 0: ");
            scanf("%i", &maximo);
            limpiaBuffer();
            cuenta(maximo, 0);
            break;
        case 1:
            printf("Usuario, ingresa un numero positivo mayor a 0: ");
            scanf("%i", &maximo);
            limpiaBuffer();
            cuenta2(maximo);
            break;
        case 2:
            printf("Adios");
            break;

        default:
            printf("Opcion no valida");
            break;
        }
        pausa();
    } while (sel != 2);

    return 0;
}

/**
 * @file main2.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-12
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>

int main()
{
    char cadena[] = "        Ani ta      lava           la   ti   na       ";

    int contador = 0;
    int idx = 0;
    bool esEspacioElAnterior = true;

    while (cadena[idx] != '\0')
    {
        if (cadena[idx] == 32 && !esEspacioElAnterior)
        {
            contador++;
            esEspacioElAnterior = true;
        }
        else
        {
            if (cadena[idx] != 32)
                esEspacioElAnterior = false;
        }
        idx++;
    }

    if (cadena[idx - 1] != 32)
        contador++;

    printf("%i", contador);

    return 0;
}

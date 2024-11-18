/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-11
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <string.h>
#include<ctype.h>
#include <stdlib.h>

void POLIndromo(char *cadena)
{
    for (int i = strlen(cadena); i >= 0; i--)
    {
        putc(cadena[i], stdout);
    }
}

int poliPalabras(char *cadena)
{
    int i = 0;
    int espacio = 0;
    while (cadena[i] != '\0')
    {
        if (cadena[i] != 32 && espacio == 0)
        {
            espacio++;
        }
        else if (cadena[i] == 32 && cadena[i + 1] != 32 && cadena[i + 1] != 0 && espacio > 0)
        {
            espacio++;
        }
        i++;
    }
    return espacio;
}

int main()
{
    char cadena[100] = "     Anita    la va        la   tina       ";
    printf("%i", poliPalabras(cadena));

    return 0;
}

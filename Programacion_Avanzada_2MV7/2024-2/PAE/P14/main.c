/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-17
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>

void aMayusculas(char *arr)
{
    int i = 0;
    while (arr[i] != '\0')
    {
        if (arr[i] >= 97 && arr[i] <= 122)
        {
            arr[i] = arr[i] - 32;
        }
        i++;
    }
}

int main()
{
    char cadena[100];
    printf("Usuario, ingrese una cadena: ");
    fgets(cadena, 100, stdin);

    aMayusculas(cadena);
    printf("%s", cadena);

    return 0;
}

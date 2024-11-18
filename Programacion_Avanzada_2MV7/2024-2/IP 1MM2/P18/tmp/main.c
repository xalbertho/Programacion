/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-10
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>
#include"../funciones/cadena.h"

void aMayusculas(char *arr) {
    int i = 0;
    while (arr[i] != '\0')
    {
        if(arr[i] >= 97 && arr[i] <= 122) {
            arr[i] -= 32;
        }
        i++;
    }
}

int main()
{
    char nombre[100];
    printf("Escriba un nombre: ");
    fgets(nombre, 100, stdin);
    //scanf("%s", nombre);

    aMayusculas(nombre);

    printf("%s\n", nombre);


    return 0;
}

/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-09
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>

void concatenarCadenas(char *cadena1, char *cadena2) {
    int i = 0, j=0;
    while(cadena1[i++] != '\0');
    i--;

    while(cadena2[j] != '\0') {
        cadena1[i] = cadena2[j];
        i++;
        j++;
    }
    cadena1[i]='\0';
}

void copiar(char origen[], char destino[])
{
    int i = 0;
    while (origen[i] != '\0')
    {
        destino[i] = origen[i];
        i++;
    }
    destino[i] = '\0';
}

void mayusculas(char *cadena)
{
    int i = 0;
    while (cadena[i] != '\0')
    {
        if (cadena[i] >= 97 && cadena[i] <= 122)
        {
            cadena[i] -= 32;
        }
        i++;
    }
}

void concatenaEnteros(int arr1[], int n1, int arr2[], int n2, int res[], int nr) {
    if((n1+n2) > nr) {
        return;
    }
    int c=0;
    for (int i = 0; i < n1; i++)
    {
        res[c++] = arr1[i];
    }
    for (int i = 0; i < n2; i++)
    {
        res[c++] = arr2[i];
    }
}

int main()
{
    char arr[100] = "Hola";
    int a[2] = {1, 2};
    int b[2] = {3,4};
    int c[4];
    concatenarCadenas(arr, " ");
    concatenarCadenas(arr, "a");
    concatenarCadenas(arr, " ");
    concatenarCadenas(arr, "todes.");


    concatenaEnteros(a,2,b,2,c,4);



    return 0;

    copiar("NiNgun0", arr);
    mayusculas(arr);

    printf("%s");

    return 0;
}

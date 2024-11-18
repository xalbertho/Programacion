/**
 * @file main2.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-15
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>
#include<string.h>

void deReversaMami(char *cadena) {
    int n = strlen(cadena);
    for (int i = n-1; i >= 0; i--)
    {
        putc(cadena[i], stdout);
    }
}

int cuentaPalabras(char *cadena) {
    int i=0, cont = 0;
    while(cadena[i] != '\0') {
        if(cadena[i] == ' ') {
            cont++;
            while(cadena[++i] == ' ');
            continue;
        }
        i++;
    }
    cont++;
    if(cadena[i-1] == ' ') cont--;
    if(cadena[0] == ' ') cont--;
    return cont;
}

int main()
{
    char cad[] = "     Un               texto  mas      palabras   ";

    printf("%i\n", cuentaPalabras(cad));

    /**char cadena[100];
    printf("Usuario, ingrese una cadena: ");
    fgets(cadena, 100, stdin);

    deReversaMami(cadena);*/
    return 0;
}

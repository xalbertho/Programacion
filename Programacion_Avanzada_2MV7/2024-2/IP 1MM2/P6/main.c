/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Programa que solicita un entero y devuelve 
 * la suma de sus digitos
 * @version 0.1
 * @date 2024-02-28
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int numero;
    int suma = 0;

    printf("Querido y muy estimado usuario, por favor ingrese un numero entero mayor a 0: ");
    scanf("%d", &numero);

    while(numero > 0) {
        suma += (numero%10);
        numero /= 10;
    }
    
    printf("La suma de los digitos es: %i\n", suma);

    return 0;
}

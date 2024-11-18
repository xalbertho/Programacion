/**
 * @file main3.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Uso de funciones de entrada y salida 3
 * @version 0.1
 * @date 2024-02-16
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int edad;
    float altura;
    char nombre[10], aux[100];

    printf("Usuario, por favor ingrese su edad: ");
    scanf("%d", &edad); // No olvidar poner el & antes del nombre de la variable

    printf("Ahora ingrese su altura: ");
    scanf("%f", &altura);

    printf("Finalmente, ingrese su nombre: ");
    //scanf("%s", nombre);
    fgets(aux,100, stdin);
    fgets(nombre, 10, stdin);

    printf("Hola %s, tu edad es: %d y tu altura es: %010.3f", nombre, edad, altura);
    return 0;
}

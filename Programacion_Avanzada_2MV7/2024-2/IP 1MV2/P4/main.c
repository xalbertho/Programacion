/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief IF
 * @version 0.1
 * @date 2024-02-22
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>

int main()
{
    int edad;

    printf("Usuario, ingresa tu edad: ");
    scanf("%d", &edad);

    if (edad < 0)
    {
        printf("No manches, esa edad es de capacidades diferentes.\n");
    }
    else if (edad >= 18 && edad <= 25)
    {
        printf("El futuro de mexico depede de tu voto este 7 de julio\n");
    }
    else if (edad > 25 && edad <= 40)
    {
        printf("Si votas te damos una despensa. Quiuvole con tu voto.\n");
    }
    else if (edad > 40 && edad <= 60)
    {
        printf("Tu eres el pasado de mexico, ya no votes por favor.\n");
    }
    else if (edad > 60)
    {
        printf("Aprovecha tu ultimo voto.\n");
    }
    else
    {
        printf("Tu voto no vale, o sea no importas\n");
    }

    return 0;
}

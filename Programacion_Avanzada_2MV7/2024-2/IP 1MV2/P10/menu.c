/**
 * @file menu.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-03-11
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>

#define PI 3.2426

int main()
{
    int opcion;

    do
    {
#if _WIN32
        system("cls");
#else
        system("clear");
#endif
        printf("Menu\n");
        printf("1. Opcion 1\n");
        printf("2. Opcion 2\n");
        printf("3. Salir\n");
        printf("Seleccione una opcion: ");
        scanf("%i", &opcion);
        while (getchar() != '\n');

        switch (opcion)
        {
        case 1:
            printf("Opcion 1\n");
            break;
        case 2:
            printf("Opcion 2\n");
            break;
        case 3:
            printf("Adios\n");
            break;
        default:
            printf("Opcion no valida\n");
            break;
        }

        printf("Presione ENTER para continua...");
        while (getchar() != '\n');
    } while (opcion != 3);

    return 0;
}

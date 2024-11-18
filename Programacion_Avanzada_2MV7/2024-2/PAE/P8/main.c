/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-03-11
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include<stdlib.h>

int main()
{
    int opcion;
    do
    {
        printf("Menu\n");
        printf("\t1. Opcion 1\n");
        printf("\t2. Opcion 2\n");
        printf("\t3. Salir\n");
        printf("Seleccione una opcion: ");
        scanf("%i", &opcion);
        getc(stdin);

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
            printf("Opcion con capacidades diferentes\n");
            break;
        }
        printf("Presione ENTER para continuar...");
        getc(stdin);
        #if _WIN32
        system("cls");
        #else
        system("clear");
        #endif

    } while (opcion != 3);

    return 0;
}

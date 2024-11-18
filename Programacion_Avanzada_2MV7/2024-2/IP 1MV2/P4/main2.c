/**
 * @file main2.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief SWITCH
 * @version 0.1
 * @date 2024-02-22
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>

int main()
{
    int seleccion;

    printf("Menu\n\t1. Opcion 1\n\t2. Opcion 2\n\t3. Opcion 3\nSeleccione una opcion: ");
    scanf("%i", &seleccion);

    /*if (seleccion == 1)
        printf("Opcion 1\n");
    else if (seleccion == 2)
        printf("Opcion 2\n");
    else if (seleccion == 3)
        printf("Opcion 3\n");
    else
        printf("Opcion no valida\n");*/

    switch (seleccion)
    {
    case 1:
        {
            int var = 10;
            printf("Opcion 1");
        }
        break;
    case 2:
        printf("Opcion 2");
        break;
    case 3:
        printf("Opcion 3");
        break;
    default:
        printf("Opcion no valida\n");
        break;
    }

    return 0;
}

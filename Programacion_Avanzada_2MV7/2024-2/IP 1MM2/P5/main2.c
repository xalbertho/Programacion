/**
 * @file main2.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief SWITCH
 * @version 0.1
 * @date 2024-02-27
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>

int main()
{
    int seleccion;

    printf("Menu\n\t1. Opcion 1\n\t2. Opcion 2\n\t3. Opcion 3\nSeleccione una occion: ");
    scanf("%i", &seleccion);

    /*if(seleccion == 1) {
        printf("Seleccionaste la opcion 1\n");
    } else if(seleccion == 2) {
        printf("Seleccionaste la opcion 2\n");
    } else if(seleccion == 3) {
        printf("Seleccionaste la opcion 3\n");
    } else {
        printf("Acaso eres tonto? Esa opcion no es valida\n");
    }*/

    switch (seleccion)
    {
    case 1:
    {
        int var = 10;
        printf("Seleccionaste la opcion 1\n");
    }
    break;
    case 2:
        printf("Seleccionaste la opcion 2\n");
        break;
    case 3:
        printf("Seleccionaste la opcion 3\n");
        break;
    default:
        printf("Acaso eres tonto? Esa opcion no es valida\n");
        // break;
    }

    return 0;
}

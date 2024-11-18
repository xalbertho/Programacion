/**
 * @file agenda.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-30
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "tools.h"
#include "libagenda.h"

int main()
{
    Contacto *lista = NULL, temp;
    int contador = 0, id;

    char *items[] = {"Agregar contacto", "Listar contactos", "Eliminar contacto", "Salir"};
    int sel;

    do
    {
        sel = showMenu(4, items, "Agenda de Contactos");

        switch (sel)
        {
        case 0:
            printf("Ingrese el nombre del contacto: ");
            fgets(temp.nombre, 500, stdin);
            quitaenters(temp.nombre);
            printf("Ingrese el apodo del contacto: ");
            fgets(temp.apodo, 100, stdin);
            quitaenters(temp.apodo);
            printf("Ingrese el telefono del contacto: ");
            fgets(temp.telefono, 30, stdin);
            quitaenters(temp.telefono);
            printf("Ingrese el correo del contacto: ");
            fgets(temp.correo, 100, stdin);
            quitaenters(temp.correo);
            printf("Ingrese la fecha de nacimiento [dd/mm/aaaa]: ");
            scanf("%i/%i/%i", &temp.fnacimiento.dia, &temp.fnacimiento.mes, &temp.fnacimiento.anio);
            limpiaBuffer();
            agregar(&lista, &contador, temp);
            break;
        case 1:
            imprimir(lista, contador);
            break;
        case 2:
            printf("Ingrese el ID a eliminar: ");
            scanf("%i", &id);
            limpiaBuffer();
            printf("Contacto %s\n", eliminar(&lista, &contador, id) ? "ELIMINADO" : "No eliminado");
            break;

        default:
            break;
        }
        pausa();
    } while (sel != 3);

    return 0;
}

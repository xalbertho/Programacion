/**
 * @file agenda.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-29
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "tools.h"

typedef struct Fecha
{
    int dia;
    int mes;
    int anio;
} Fecha;

typedef struct Contacto
{
    char nombre[100];
    char apodo[50];
    char telefono[20];
    char correo[100];
    Fecha fnacimiento;
} Contacto;

void agregar(Contacto **lista, int *tamanio, Contacto con)
{
    if (*lista == NULL)
    {
        *lista = (Contacto *)malloc(sizeof(Contacto));
        strcpy((*lista)->nombre, con.nombre);
        strcpy((*lista)->apodo, con.apodo);
        strcpy((*lista)->telefono, con.telefono);
        strcpy((*lista)->correo, con.correo);
        (*lista)->fnacimiento.dia = con.fnacimiento.dia;
        (*lista)->fnacimiento.mes = con.fnacimiento.mes;
        (*lista)->fnacimiento.anio = con.fnacimiento.anio;
        (*tamanio)++;
    }
    else
    {
        *lista = realloc(*lista, (*tamanio + 1) * sizeof(Contacto));
        strcpy((*lista + *tamanio)->nombre, con.nombre);
        strcpy((*lista + *tamanio)->apodo, con.apodo);
        strcpy((*lista + *tamanio)->telefono, con.telefono);
        strcpy((*lista + *tamanio)->correo, con.correo);
        (*lista + *tamanio)->fnacimiento.dia = con.fnacimiento.dia;
        (*lista + *tamanio)->fnacimiento.mes = con.fnacimiento.mes;
        (*lista + *tamanio)->fnacimiento.anio = con.fnacimiento.anio;
        (*tamanio)++;
    }
}

void imprimir(Contacto *lista, int tamanio)
{
    printf("LISTA DE CONTACTOS\n\n");
    for (int i = 0; i < tamanio; i++)
    {
        printf("%5i. %s       %s       %s       %s", i + 1, (lista + i)->nombre, (lista + i)->apodo, (lista + i)->telefono, (lista + i)->correo);
        printf("       %02i/%02i/%04i\n", (*(lista + i)).fnacimiento.dia, (*(lista + i)).fnacimiento.mes, (*(lista + i)).fnacimiento.anio);
    }
}

bool eliminar(Contacto **lista, int *cont, int id)
{
    if (*lista == NULL)
    {
        return false;
    }
    else
    {
        if (id < 1 || id > *cont)
        {
            return false;
        }
        else
        {
            if (*cont == 1)
            {
                free(*lista);
                *cont = 0;
                *lista = NULL;
                return true;
            }
            else
            {
                memcpy((*lista + (id - 1)), (*lista + id), (*cont - id) * sizeof(Contacto));
                *lista = realloc(*lista, (*cont - 1) * sizeof(Contacto));
                (*cont)--;
                return true;
            }
        }
    }
}

int main()
{
    Contacto *lista = NULL, tmp;

    int tamanio = 0, sel = 0, id;

    char *items[] = {"Agregar contacto", "Listar contactos", "Eliminar contacto", "Salir"};

    do
    {
        sel = showMenu(4, items, "Agenda de Contactos");
        switch (sel)
        {
        case 0:
            printf("Ingrese el nombre: ");
            fgets(tmp.nombre, 100, stdin);
            printf("Ingrese el apodo: ");
            fgets(tmp.apodo, 50, stdin);
            printf("Ingrese el numero: ");
            fgets(tmp.telefono, 20, stdin);
            printf("Ingrese el correo: ");
            fgets(tmp.correo, 100, stdin);
            printf("Ingrese la fecha de nacimiento (dd/mm/aaaa): ");
            scanf("%i/%i/%i", &tmp.fnacimiento.dia, &tmp.fnacimiento.mes, &tmp.fnacimiento.anio);
            limpiaBuffer();
            agregar(&lista, &tamanio, tmp);
            break;
        case 1:
            imprimir(lista, tamanio);
            break;
        case 2:
            printf("Ingrese el id a eliminar: ");
            scanf("%i", &id);
            limpiaBuffer();
            if (eliminar(&lista, &tamanio, id))
            {
                printf("Contacto eliminado.");
            }
            else
            {
                printf("No fue posible eliminar el contacto especificado.");
            }
            break;

        default:
            break;
        }
        pausa();
    } while (sel != 3);

    return 0;
}

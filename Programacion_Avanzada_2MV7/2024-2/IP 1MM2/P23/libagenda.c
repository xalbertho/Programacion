#include"libagenda.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void agregar(Contacto **lista, int *contador, Contacto c)
{
    if (*lista == NULL)
    {
        *lista = malloc(sizeof(Contacto));
        strcpy((*lista)->nombre, c.nombre);
        strcpy((*lista)->apodo, c.apodo);
        strcpy((*lista)->correo, c.correo);
        strcpy((*lista)->telefono, c.telefono);
        (*lista)->fnacimiento.dia = c.fnacimiento.dia;
        (*lista)->fnacimiento.mes = c.fnacimiento.mes;
        (*lista)->fnacimiento.anio = c.fnacimiento.anio;

        *contador = 1;
    }
    else
    {
        *lista = realloc(*lista, (*contador + 1) * sizeof(Contacto));
        strcpy((*lista + *contador)->nombre, c.nombre);
        strcpy((*lista + *contador)->apodo, c.apodo);
        strcpy((*lista + *contador)->correo, c.correo);
        strcpy((*lista + *contador)->telefono, c.telefono);
        (*lista + *contador)->fnacimiento.dia = c.fnacimiento.dia;
        (*lista + *contador)->fnacimiento.mes = c.fnacimiento.mes;
        (*lista + *contador)->fnacimiento.anio = c.fnacimiento.anio;
        (*contador)++;
    }
}

void imprimir(Contacto *lista, int cont)
{
    for (int i = 0; i < cont; i++)
    {
        printf("%i. %s\n   %s\n   %s\n   %s\n   %02i/%02i/%04i\n",
               i + 1, (lista + i)->nombre, (lista + i)->apodo,
               (lista + i)->telefono, (lista + i)->correo,
               (lista + i)->fnacimiento.dia, (lista + i)->fnacimiento.mes,
               (lista + i)->fnacimiento.anio);
    }
}

void quitaenters(char *cadena)
{
    cadena[strlen(cadena) - 1] = '\0';
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
                memcpy(*lista + id - 1, *lista + id, (*cont - id) * sizeof(Contacto));
                *lista = realloc(*lista, (*cont - 1) * sizeof(Contacto));
                (*cont)--;
                return true;
            }
        }
    }
}

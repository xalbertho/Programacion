/**
 * @file libagenda.h
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-05-03
 * 
 * @copyright Copyright (c) 2024
 * 
 */

#ifndef __LIBAGENDA_H__
#define __LIBAGENDA_H__

#include<stdbool.h>

typedef struct Fecha
{
    int dia;
    int mes;
    int anio;
} Fecha;

typedef struct Contacto
{
    char nombre[500];
    char apodo[100];
    char telefono[30];
    char correo[100];
    Fecha fnacimiento;
} Contacto;

/**
 * @brief 
 * 
 * @param lista 
 * @param contador 
 * @param c 
 */
void agregar(Contacto **lista, int *contador, Contacto c);
/// @brief 
/// @param lista 
/// @param cont 
void imprimir(Contacto *lista, int cont);
/// @brief 
/// @param cadena 
void quitaenters(char *cadena);
/**
 * @brief 
 * 
 * @param lista 
 * @param cont 
 * @param id 
 * @return true 
 * @return false 
 */
bool eliminar(Contacto **lista, int *cont, int id);

#endif

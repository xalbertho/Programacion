/**
 * @file fmaizoro.h
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Archivo de encabezado
 * @version 0.1
 * @date 2024-03-19
 * 
 * @copyright Copyright (c) 2024
 * 
 */

#ifndef __FMAIZORO_H__
#define __FMAIZORO_H__

// Declaracion

/**
 * @brief Suma dos numeros
 *
 * @param a Primer numero
 * @param b Segundo numero
 * @return float La suma
 */
float suma(float a, float b);

float sumaRef(float *a, float *b);

void maizoro(float a, float b, float *suma, float *resta, float *mult, float *divi);

#endif
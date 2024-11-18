#ifndef __MAIZORO_H__
#define __MAIZORO_H__

// Declaracion

/**
 * @brief Suma dos numeros
 * 
 * @param a Numero 1
 * @param b Numero 2
 * @return float Suma de Numero 1 y Numero 2
 */
float suma(float *a, float *b);

float sumaValor(float a, float b);

/**
 * @brief 
 * 
 * @param a 
 * @param b 
 * @param suma 
 * @param resta 
 * @param multi 
 * @param divi 
 */
void maizoro(float a, float b, float *suma, float *resta, float *multi, float *divi);

#endif
/**
 * @file biblioteca.h
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-03-27
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#ifndef __BIBLIOTECA_H__
#define __BIBLIOTECA_H__

/**
 * @brief Ordena un arreglo por el metodo de la burbuja
 * 
 * @param arr El arreglo
 * @param n El tamanio del arreglo
 */
void ordena(int *arr, int n);

/**
 * @brief Obtiene el numero de digitos de un numero entero
 * 
 * @param numero El numero
 * @param resultado El resultado
 */
void noDigitos(int numero, int *resultado);

/**
 * @brief Suma los digitos de un numero entero
 * 
 * @param numero El numero
 * @param resultado El resultado
 */
void sumaDigitos(int numero, int *resultado);

/**
 * @brief Busca un numero en un arreglo de forma no binaria (inclusion forzada)
 * 
 * @param arr El arreglo
 * @param inf Limite inferior
 * @param sup Limite superior
 * @param x El perdido
 * @param res El resultado
 */
void busquedaBinaria(int *arr, int inf, int sup, int x, int *res);

#endif
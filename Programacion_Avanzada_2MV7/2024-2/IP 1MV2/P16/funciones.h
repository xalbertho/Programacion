/**
 * @file funciones.h
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-03-26
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#ifndef __FUNCIONES_H__
#define __FUNCIONES_H__

/**
 * @brief Cuenta el numero de digitos de un long sin signo
 * 
 * @param numero El numero
 * @param contador El contador
 */
void noDigitos(unsigned long numero, unsigned long *contador);

/**
 * @brief Suma los digitos de un numero
 * 
 * @param numero El numero
 * @param suma La suma
 */
void sumaDigitos(unsigned long numero, unsigned long *suma);

/**
 * @brief Ordena un arreglo de tamanio n por el metodo de la burbuja.
 * 
 * @param arr El arreglo
 * @param n El tamanio del arreglo
 */
void burbuja(int *arr, int n);

/**
 * @brief Genera un arreglo de numeros pseudoaleatorios
 * 
 * @param arr El arreglo
 * @param n El tamanio
 */
void generar(int *arr, int n);

/**
 * @brief Imprime un arreglo
 * 
 * @param arr El arreglo
 * @param n El tamnio del arreglo
 */
void imprime(int arr[], int n);
#endif
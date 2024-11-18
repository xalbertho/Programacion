/**
 * @file funciones.h
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Mi biblioteca de funciones
 * @version 0.1
 * @date 2024-03-26
 *
 * @copyright Copyright (c) 2024
 *
 */

#ifndef __FUNCIONES_H__
#define __FUNCIONES_H__
/**
 * @brief Genera un arreglo de N numeros pseudoaleatorios
 *
 * @param arreglo El arreglo
 * @param n El tamanio
 */
void generar(int *arreglo, int n);

/**
 * @brief Imprime un arreglo de tamaño N
 *
 * @param arreglo El arreglo a imprimir
 * @param n El tamanio del arreglo
 */
void imprimir(int arreglo[], int n);

/**
 * @brief Encuentra el elemento mas grande de un arreglo 
 * 
 * @param arreglo El arreglo
 * @param n El tamaño del arreglo
 * @return int El elemento mas grande
 */
int elmasgrande(int *arreglo, int n);

#endif
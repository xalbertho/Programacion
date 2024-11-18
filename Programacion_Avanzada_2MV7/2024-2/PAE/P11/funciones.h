/**
 * @file funciones.h
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-03-27
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#ifndef __FUNCIONES_H__
#define __FUNCIONES_H__

/**
 * @brief Genera un arreglo de tamanio N con numeros pseudoaleatorios
 * 
 * @param arrg El arreglo
 * @param n El n
 */
void genera(int *arrg, int n);

/**
 * @brief Imprime un arreglo de tamanio N
 * 
 * @param arrg El arreglo
 * @param n La n
 */
void imprime(int arrg[], int n);

/**
 * @brief Imprime del 0 a N
 * 
 * @param n El maximo valor a imprimir
 * @param i El contador. 0 la primera vez
 */
void cuenta(int n, int i);

/**
 * @brief Los mismo que la anterior pero mas chido
 * 
 * @param n El maximo
 */
void cuenta2(int n);

#endif
/**
 * @file recursion.h
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-12
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#ifndef __RECURSION_H__
#define __RECURSION_H__

/**
 * @brief Imprime el arreglo
 * 
 * @param arr 
 * @param n 
 */
void imprime(int *arr, int n);

/**
 * @brief Ordena por burbuja
 * 
 * @param arr 
 * @param n 
 */
void burburja(int *arr, int n);

/**
 * @brief Busca un numero
 * 
 * @param arr 
 * @param inicio 
 * @param x 
 * @return int 
 */
int busca(int *arr, int inicio, int final, int x);

#endif
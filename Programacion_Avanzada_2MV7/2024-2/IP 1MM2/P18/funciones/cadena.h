/**
 * @file cadena.h
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-10
 * 
 * @copyright Copyright (c) 2024
 * 
 */

#ifndef __CADENA_H__
#define __CADENA_H__
/**
 * @brief Copia la cadena origen en la cadena destino
 * 
 * @param origen Origen
 * @param destino Destino
 */
void copiar(char *origen, char *destino);
/**
 * @brief Concatena la cadena2 en la cadena1
 * 
 * @param cadena1 Cadena1
 * @param cadena2 Cadena2
 */
void concatena(char *cadena1, char *cadena2);
/**
 * @brief Devuelve el tamanio de una cadena
 * 
 * @param candena La cadena
 * @return int El tamanio
 */
int tamanio(char *candena);

#endif
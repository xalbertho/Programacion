/**
 * @file funciones.hpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-29
 * 
 * @copyright Copyright (c) 2024
 * 
 */

#ifndef __FUNCIONES_HPP__
#define __FUNCIONES_HPP__

/**
 * @brief 
 * 
 */
class Fecha
{
private:
    unsigned char _dia;
    unsigned char _mes;
    unsigned short _anio;

public:
    Fecha(int dia, int mes, int anio);

    /**
     * @brief 
     * 
     * @param dia 
     */
    void dia(int dia);

    /// @brief 
    /// @return 
    int dia();

    /// @brief 
    /// @param mes 
    void mes(int mes);

    int mes();

    void anio(int anio);

    int anio();
};

#endif
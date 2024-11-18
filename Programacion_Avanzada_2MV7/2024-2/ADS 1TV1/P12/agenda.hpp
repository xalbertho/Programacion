/**
 * @file agenda.hpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Biblioteca de agenda de contactos
 * @version 0.1
 * @date 2024-03-26
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#ifndef __AGENDA_HPP__
#define __AGENDA_HPP__

#include <iostream>
#include <vector>

using namespace std;

namespace agenda
{
    class Contacto
    {
    private:
        string nombre, apodo, numero;

    public:
        Contacto(string nombre, string apodo, string numero) : nombre(nombre), apodo(apodo), numero(numero) {}

        // getters
        string getNombre();
        string getApodo();
        string getNumero();

        // setters
        void setNombre(string nombre);
        void setApodo(string apodo);
        void setNumero(string numero);
    };

    class Agenda
    {
    private:
        vector<Contacto> lista;

    public:
        // Metodos

        /**
         * @brief Agrega un contacto a la agenda
         * 
         * @param nombre Nombre del contacto
         * @param apodo Apodo del contacto
         * @param numero Numero del contacto
         */
        void agregar(string nombre, string apodo, string numero);

        /**
         * @brief Busca un contacto por nombre
         * 
         * @param nombre El nombre a buscar
         * @return int ID del contacto o -1 si no lo encuentra.
         */
        int buscarPorNombre(string nombre);

        /**
         * @brief Busca un contacto por apodo
         * 
         * @param apodo El apodo a buscar
         * @return int ID del contacto o -1 si no lo encuentra.
         */
        int buscarPorApodo(string apodo);

        /**
         * @brief Actualiza un contacto
         * 
         * @param id ID del contacto a actualizar
         * @param nombre Nuevo nombre
         * @param apodo Nuevo apodo
         * @param numero Nuevo numero
         */
        void actualizar(int id, string nombre, string apodo, string numero);

        /**
         * @brief Devuelve la lista de contactos
         * 
         * @return string String con la informacion de los contactos
         */
        string listar();

        /**
         * @brief Llama a un contacto
         * 
         * @param idx ID del contacto
         * @return string Llamada
         */
        string llamar(int idx);
    };

} // namespace agenda

#endif
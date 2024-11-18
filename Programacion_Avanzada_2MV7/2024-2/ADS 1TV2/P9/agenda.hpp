/**
 * @file agenda.hpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
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

        // setter
        void setNombre(string nombre);
        void setApodo(string apodo);
        void setNumero(string numero);
    };

    class Agenda
    {
    private:
        vector<Contacto> lista;

    public:
        /**
         * @brief Agrega un nuevo contacto a la agenda
         * 
         * @param nombre Nombre del contacto
         * @param apodo Apodo del contacto
         * @param numero Numero telefonico
         */
        void agregarContacto(string nombre, string apodo, string numero);

        /**
         * @brief Busca un contacto por nombre. Si lo encuentra
         * devuelve su ID. Sino devuelve -1/
         * 
         * @param nombre Nombre del contacto a buscar
         * @return int ID del contacto o -1 si no existe.
         */
        int buscarPorNombre(string nombre);

        /**
         * @brief Busca un contacto por apodo. Si lo encuentra
         * devuelve su ID. Sino devuelve -1/
         * 
         * @param apodo Apodo del contacto a buscar
         * @return int ID del contacto o -1 si no existe.
         */
        int buscarPorApodo(string apodo);

        /**
         * @brief Actualiza los datos de un contacto
         * 
         * @param idx ID del contacto a actualizar
         * @param nombre Nuevo nombre del contacto
         * @param apodo Nuevo apodo del contacto
         * @param numero Nuevo numero del contacto
         */
        void actualizar(int idx, string nombre, string apodo, string numero);

        /**
         * @brief Genera una lista con los datos de todos los contactos
         * 
         * @return string Lista de contactos
         */
        string listar();

        /**
         * @brief Llama a un contacto
         * 
         * @param id ID del contacto
         * @return string Resultado
         */
        string llamar(int id);
    };

} // namespace agenda

#endif

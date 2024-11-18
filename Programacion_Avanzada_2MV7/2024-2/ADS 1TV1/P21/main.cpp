/**
 * @file main.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-30
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<iostream>
#include"miniwin.hpp"

using namespace std;
using namespace miniwin;

int main()
{
    int t = NINGUNA;
    float x,y;
    vventana(500, 300);
    vtitulo("Analisis y Disenio de Sistemas");
    color_fondo(BLANCO);
    
    t = tecla();
    while(t != ESCAPE){
        borra();

        raton(x, y);


        color_rgb(50,25,200);
        rectangulo_lleno(x,y,x+50, y+30);

        color(ROJO);
        linea(3,4,200,189);

        texto(4,5,"Hola a todos");

        color(NEGRO);
        texto(4,50, "Hola Mundo",50, true, true, true, "Arial");
        
        t = tecla();
        refresca();
        espera(20);
    }
    vcierra();
    return 0;
}

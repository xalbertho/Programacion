#include"miniwin.hpp"
#define GRAVEDAD 1

using namespace miniwin;

int main()
{
    int t;
    float x,y;
    int rx = 50, ry = 50, salto = 0;
    bool on=false, ip = false, dp = false;
    MiniWinImage omero("omero.bmp", "omerom.bmp");
    //omero.alto(omero.alto()/2);
    //omero.ancho(omero.ancho()/2);


    ventana(500,500);
    titulo("Mi primer juego");
    color_fondo(ROJO);

    t = tecla();

    while( t != ESCAPE) {
        borra();

        

        //color(NEGRO);
        texto(5,5,"Presione ESCAPE para salir", 50,
        true, true, true, "Comic Sans MS");


        salto += GRAVEDAD;
        ry += salto;
        if(ry+omero.alto() > valto()) ry = valto() - omero.alto();

        if(dp) rx+=10;
        if(ip) rx-=10;

        if(rx+omero.ancho() > vancho()) rx = vancho()-omero.ancho();
        if(rx < 0) rx = 0;
        
        t=teclaDown();



        if(t == RETURN) {
            on = !on;
            fullscreen(on);
        }

        if(t == DERECHA) {
            dp = true;
        }
        if(t == IZQUIERDA) {
            ip = true;
        }

        if(t == ESPACIO) {
            salto = -20;
        }

        t = teclaUp();
        if(t == DERECHA) {
            dp = false;
        }
        if(t == IZQUIERDA) {
            ip = false;
        }

        

        raton(x,y);

        color(Colores::NEGRO);
        circulo_lleno(x,y, 10);

        color(Colores::BLANCO);
        //rectangulo_lleno(rx,ry, rx+50,ry+50);
        omero.posX(rx);
        omero.posY(ry);
        muestraImagen(omero);



        refresca();
        espera(1);
    }
    cierra();
    return 0;
}

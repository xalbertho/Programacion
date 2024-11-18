#include"miniwin.hpp"
#define GRAVEDAD 1
using namespace miniwin;

int main()
{
    int t, radio = 30, impulso = 0;
    float x = 50,y = 50, rx=0, ry=0;
    bool on = false;
    bool izquierda = true;
    bool ip = false, dp = false;
    MiniWinImage vanessa("vanessa.bmp", "vanessam.bmp");
    MiniWinImage vanessal("vanessal.bmp", "vanessaml.bmp");

    vanessa.posX(0);
    vanessa.posY(0);
    vanessal.posX(0);
    vanessal.posY(0);

    //vanessa.alto(vanessa.alto()/4);
    //vanessa.ancho(vanessa.ancho()/4);
    


    titulo("Mi Primer Juego");
    ventana(500,500);
    color_fondo(Colores::MAGENTA);
    

    t = tecla();
    while(t != Teclas::ESCAPE) {

        impulso += GRAVEDAD;
        y+=impulso;
        if((y + vanessa.alto()) > valto()) y = valto() - vanessa.alto();
        if(dp) x+=10;
        if(ip) x-=10;

        if((x + vanessa.ancho()) > vancho()) x = vancho() - vanessa.ancho();
        if(x < 0) x = 0;



        if(t == Teclas::RETURN) {
            on = !on;
            fullscreen(on);
        }

        if(t == Teclas::ESPACIO) {
            impulso = -20;
        }

        borra();

        texto(5,5, "Presione ESC para salir", 50, false, true, false, "Segoe Script");

        raton(rx, ry);

        vanessa.posX(x);
        vanessa.posY(y);
        vanessal.posX(x);
        vanessal.posY(y);
        color(Colores::NEGRO);
        circulo_lleno(rx,ry, radio);

        t = teclaDown();
        if(t == DERECHA) {
            dp = true;
            izquierda = false;
        }
        if(t == IZQUIERDA) {
            ip = true;
            izquierda = true;
        }

        t = teclaUp();
        if(t == DERECHA) dp = false;
        if(t == IZQUIERDA) ip = false;

        //color(BLANCO);
        //rectangulo_lleno(100,200,150, 400);

        if(izquierda)
        muestraImagen(vanessal);
        else
        muestraImagen(vanessa);


        refresca();
        
        espera(1);
    
    }
    cierra();
    
    return 0;
}

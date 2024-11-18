#include "sims.hpp"

int main()
{
    Sim c("Intel",232);
    Sim d("AMD",132);

    Celular com("Xiamomi","Mi 11",212,"samsung");
    com.Agregar(c);
    com.Agregar(d);
    com.muestra();
    
}
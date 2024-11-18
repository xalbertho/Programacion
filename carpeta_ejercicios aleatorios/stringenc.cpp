#include <stdio.h>
#include <string.h>
#include <ctype.h>


int main(void){
    char nombre[20]; printf("iNGRESE SU NOMBRE");

    char iniciales[5];
    int contador=0;

    printf("iNGRESE SU NOMBRE");
    gets(nombre);

    for (int i=0; strlen(nombre); i++){
        if (isupper(nombre[i])){
        iniciales[contador]=nombre[i];
          contador++;
        }
    contador++;
    }

    iniciales[contador]='\0';

   printf("%s\n",iniciales);
}

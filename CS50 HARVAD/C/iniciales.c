//#include <cs50.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>


int main(void){
    char nombre[20]={0}; 
    char iniciales[5]={0};
    int contador=0;

    printf("iNGRESE SU NOMBRE: ");
    gets(nombre);

int longitud=strlen(nombre); 

    for (int i=0; i<strlen(nombre); i++){

        if (isupper(nombre[i])){
        iniciales[contador]=nombre[i];
          contador++;
        }
    
    }

    iniciales[contador]='\0';

  printf("%s\n",iniciales);
}
#include <Stdio.h>
#include <cs50.h>

int main(){

    float promedio,alturas[7],suma=0;
    int contador=0;

    for(int i=0;i<5;i++){
        printf("Ingrese la altura numero, %d: ",i+1);
        scanf("%f",&alturas[i]);
        suma+=alturas[i];
        
    }
    promedio=suma/5;

    for(int i=0; i<5;i++){
        if (alturas[i]<promedio)
            contador++;
    }


    printf("El promedio de las alturas ingresadas es: %.2f",promedio);
    printf("Hay %d personas con altura por debajo del promedio",contador);
     printf("Hay %d personas con altura por encima del promedio",5-contador);





return 0;}

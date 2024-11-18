#include <stdio.h>

int main(){
    float sueldo_m[4],sueldo_v[4],suma1,suma2;

    for(int i=0; i<4;i++){
        printf("Ingrese el salaro del empleado %d (turno matutino): ",i+1);
        scanf("%f",&sueldo_m[i]);
        suma1+=sueldo_m[i];

    }

     for(int i=0; i<4;i++){
        printf("Ingrese el salaro del empleado %d (turno vespertino): ",i+1);
        scanf("%f",&sueldo_v[i]);
        suma2+=sueldo_v[i];

    }

printf("El gasto total de los empleados en el turno matutino es de: %.2f",suma1);
printf("\nEl gasto total de los empleados en el turno vespertino es de: %.2f",suma2);





return 0;}

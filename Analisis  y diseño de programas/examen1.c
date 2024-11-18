
/*
JOSE ALBERTO BARRIOS MENDEZ
BOLETA: 2022640111
EXAMEN 1
*/

#include <stdio.h>

struct Dron
{
    int num_seri;
    char falla[20]; 
};

void imprimir(struct Dron drones[], int n); 

int main(void)
{
    int i = 0;
    char respuesta;
    struct Dron drones[10]; 

    while (1)
    {
        printf("Ingrese el numero de serie del dron: \n");
        scanf("%d", &drones[i].num_seri);
        printf("Ingrese la falla para este dron\n1.GPS\n2.CONTROLADOR\n3.HELICES\n4.SENSORES\n5.MARCO\n6.MOTORES \n");
        scanf("%s", drones[i].falla);

        printf("Desea agregar otro dron? s/n: "); 
        scanf(" %c", &respuesta); // 

        if (respuesta != 's')
        {
            break;
        }
        else
        {
            i++; 
            continue;
        }
    }
    printf("\n\nLos drones ingresados con sus fallas son: \n");
    imprimir(drones, i); 
}

void imprimir(struct Dron drones[], int n) 
{
    for (int i = 0; i < n; i++)
    {
        printf("Numero de serie: %d con falla en: %s\n", drones[i].num_seri, drones[i].falla);
    }
}

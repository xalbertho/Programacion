#include <stdio.h>
#include <ctype.h>

struct Materias 
{
    int numero_materias_reprobadas;
    char nombre[30];
    char Materia[20][20];
};

int main(void) {
    struct Materias mat_r[20];
    char respuesta;

    int i = 0;

    while (1) 
    {
        printf("Ingrese su nombre: \n");
        scanf("%s", mat_r[i].nombre);
    printf("Ingrese el numero de materias reprobadas: \n");
        scanf("%d", &mat_r[i].numero_materias_reprobadas);

        for (int k = 0; k < mat_r[i].numero_materias_reprobadas; k++) 
        {
            printf("Ingrese la materia reprobada: ");
            scanf("%s", mat_r[i].Materia[k]);
        }

        printf("Desea guardar otro alumno?: (s/n)\n");
        scanf(" %c", &respuesta);

        if (tolower(respuesta) != 's') 
        {
            break;
        }

        i++;
    }

 printf("Las materias reprobadas son:\n");

    for (int j = 0; j <= i; j++) { 
        printf("Alumno: %s\n", mat_r[j].nombre);
     printf("Materias reprobadas:\n");

        for (int k = 0; k < mat_r[j].numero_materias_reprobadas; k++) {
            printf("%s\n", mat_r[j].Materia[k]);
        }
        printf("\n");
    }

}
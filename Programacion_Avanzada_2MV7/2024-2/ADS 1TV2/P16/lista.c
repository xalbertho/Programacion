#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

void agregar(int **lista, int *cont, int valor) {
    if(*lista == NULL) {
        *lista = malloc(sizeof(int));
        **lista = valor;
        *cont = 1;
    } else {
        *lista = realloc(*lista, (*cont + 1) * sizeof(int));
        *(*lista + *cont) = valor;
        (*cont)++;
    }
}


bool lista_vacia(int *lista) {
    if(lista == NULL) {
        return true;
    } else {
        return false;
    }
}

void imprime(int *lista, int cont) {
    printf("\n[ ");
    for (int i = 0; i < cont; i++)
    {
        printf("%i ", *(lista+i));
    }
    printf("]\n");
}


int main()
{
    int *lista = NULL;
    int cont = 0;

    agregar(&lista, &cont, 3);
    agregar(&lista, &cont, 13);
    agregar(&lista, &cont, 13);
    agregar(&lista, &cont, 13);
    agregar(&lista, &cont, 13);
    agregar(&lista, &cont, 13);

    printf("%s\n", (lista_vacia(lista) ? "Lista VACIA": "Lista NO vacia"));

    imprime(lista, cont);
    


    
    return 0;
}

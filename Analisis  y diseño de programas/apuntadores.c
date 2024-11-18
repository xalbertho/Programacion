 #include <stdio.h>
 #include <stdlib.h>
 #include <conio.h>

 void mostrar();
 void insertar();

 struct Estudiante {
    int boleta;
    struct Estudiante *SIG;    //Apuntador de tipo estructura
                            //En SIG guardamos una direccion de memoria
};

struct Estudiante *Inicio, *Final, *Aux;
int main(){
    Inicio=(struct Estudiante *) malloc(sizeof(struct Estudiante));
    Final=Inicio;
    char Opcion = 's';
    while (Opcion != 'n'){
        insertar();
        printf("\nDeseas continuar? s/n");
        Opcion = getche();
}
Final->SIG = NULL;
mostrar();
   
}

void insertar()    {
    printf("Ingresa el número de boleta");
    scanf("%d",&Final->boleta);
    Final->SIG = (struct Estudiante *)malloc(sizeof(struct Estudiante));
    Final = Final->SIG;
}

void mostrar(){
    for(Aux=Inicio;Aux!=Final;Aux=Aux->SIG)
        printf("%d \n",Aux->boleta);
}
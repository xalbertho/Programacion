#include <stdio.h>

void solicitar_matriz(int mat[10][10],int filas, int columnas){

    for(int i=0;i<filas;i++){
        for(int j=0;j<columnas;j++){
            printf("\nIngrese el valor (%d,%d) de la matriz: ",i+1,j+1); scanf("%d",&mat[i][j]);
        }
    }

}

void imprime_matriz(int mat[10][10],int filas, int columnas){

     for(int i=0;i<filas;i++){

        for(int j=0;j<columnas;j++){
            printf("%d ",mat[i][j]);
        }
        printf("\n");
    }

}



void menu(){
    printf("Elige una operacion a realizar: \n1.Suma\n2.resta\n3.Multiplicacion\n4.Hacer matriz identidad\n5.Trasponer una matriz\n6.Inversa");
}

void suma(int mat1[10][10], int mat2[10][10],int filas, int columnas, int resultado[10][10]){
    for(int i=0; i<filas;i++){
        for(int j=0; j<columnas;j++){
            resultado[i][j]=mat1[i][j]+mat2[i][j];
        }
    }

    printf("La sua de las matrices es: \n");
    imprime_matriz(resultado,filas, columnas);

}


void resta(int mat1[10][10], int mat2[10][10],int filas, int columnas, int resultado[10][10]){
    for(int i=0; i<filas;i++){
        for(int j=0; j<columnas;j++){
            resultado[i][j]=mat1[i][j]-mat2[i][j];
        }
    }

    printf("La sua de las matrices es: \n");
    imprime_matriz(resultado,filas, columnas);

}




void multi(int mat1[10][10], int mat2[10][10], int filas, int columnas, int resultado[10][10]) {
    // Itera sobre las filas de la primera matriz
    for (int i = 0; i < filas; i++) {
        // Itera sobre las columnas de la segunda matriz
        for (int j = 0; j < columnas; j++) {
            // Inicializa el elemento en (i, j) del resultado en 0
            resultado[i][j] = 0;

            // Itera sobre las columnas de la primera matriz o las filas de la segunda matriz
            for (int k = 0; k < columnas; k++) {
                // Multiplica los elementos correspondientes y suma al resultado acumulado
                resultado[i][j] += mat1[i][k] * mat2[k][j];
            }
        }
    }

    // Imprime el resultado
    printf("\nLa Multiplicacion de las matrices es: \n");
    imprime_matriz(resultado, filas, columnas);
}

void hacer_identidad(int mat[10][10],int filas, int columnas, int resultado[10][10]){

   for(int i=0; i<filas;i++){
        for(int j=0;j<columnas;j++){
            resultado[i][j]=0;
        }
   }

   for(int i=0; i<filas;i++){
        for(int j=0;j<columnas;j++){
            if(i==j){
                resultado[i][j]=1;
            }else continue;

        }
        printf("\n");
   }

    imprime_matriz(resultado,filas,columnas);
}

void transponer_matriz(int mat1[10][10], int mat2[10][10], int filas, int columnas,int resultado[10][10]){
    int opcion=0;
    imprime_matriz(mat1,filas,columnas);
    printf("\n");
    imprime_matriz(mat2,filas,columnas);

    printf("\nQue matriz desea trasponer?\n1.Matriz 1\n2.Matriz 2\n"); scanf("%d",&opcion);
    switch(opcion){
        case 1:
            for(int i=0;i<filas;i++){
                for(int j=0;j<columnas;j++){
                    resultado[j][i]=mat1[i][j];
                }
            }
            imprime_matriz(resultado,filas,columnas);
        break;
        case 2:
            for(int i=0;i<filas;i++){
                for(int j=0;j<columnas;j++){
                    resultado[j][i]=mat2[i][j];
                }
            }
            imprime_matriz(resultado,filas,columnas);

        break;
        default :
        printf("\nopcion no valida");
    }

}

int main(){
    int mat1[10][10],mat2[10][10],filas=0,columnas=0,opcion=0,resul[10][10];
    printf("Ingrese el numero de filas de la matriz; "); scanf("%d",&filas);  printf("Ingrese el numero de columnas de la matriz: "); scanf("%d",&columnas);
    printf("Ingresa la matriz 1: \n"); solicitar_matriz(mat1,filas,columnas);
    printf("Ingresa los valores de la matriz 2: \n"); solicitar_matriz(mat2,filas,columnas);

    menu();
    printf("\nQue operacion desea realizar"); scanf("%d",&opcion);

    switch (opcion)
    {
        case 1:
            suma(mat1,mat2,filas,columnas,resul);
            break;
        case 2:
            resta(mat1,mat2,filas,columnas,resul);
           break;
        case 3:
            multi(mat1,mat2,filas,columnas,resul);
            break;
        case 4:
             hacer_identidad(mat1,filas,columnas,resul);
            break;
        case 5:
        transponer_matriz(mat1,mat2,filas,columnas,resul);
            break;


    }



    return 0;
}

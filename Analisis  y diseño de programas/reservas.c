#include <stdio.h>
#include <ctype.h>

void menu() {
    printf("Bienvenido a la aerolinea\nSeleccione la clase en la que desea viajar:\n1. Primera clase\n2. Economico\n");
}

void imprimir(int num_asiento, int primera_clase) {
    printf("----- PASE DE ABORDAJE -----\n");
    printf("Numero de asiento: %d\n", num_asiento);
    if (primera_clase) {
        printf("Sección: Primera Clase\n");
    } else {
        printf("Seccion: Economico\n");
    }
    printf("-----------------------------\n");
}

int main(void) {
    int asientos[10] = {0};
    int respuesta = 0;
    int asientos_p_c = 5;
    char resp;

    while (1) {
        menu();
        scanf("%d", &respuesta);

        if (respuesta == 1) {
            for (int i = 0; i < asientos_p_c; i++) {
                if (asientos[i] == 0) {
                    asientos[i] = 1;
                    imprimir(i + 1, 1);
                    break;
                } else if (i == asientos_p_c - 1) {
                    printf("Primera clase llena. ¿Aceptar asiento en Económico? (s/n) ");
                    scanf(" %c", &resp); // Espacio antes del %c para ignorar espacios en blanco y saltos de línea
                    resp = tolower(resp);
                    if (resp == 's') {
                        for (int j = asientos_p_c; j < 10; j++) {
                            if (asientos[j] == 0) {
                                asientos[j] = 1;
                                imprimir(j + 1, 0);
                                break;
                            }
                        }
                    } else {
                        printf("El siguiente vuelo sale en 3 horas...\n");
                        break; // Salir del bucle
                    }
                }
            }
        } else if (respuesta == 2) {
            for (int i = asientos_p_c; i < 10; i++) {
                if (asientos[i] == 0) {
                    asientos[i] = 1;
                    imprimir(i + 1, 0);
                    break;
                } else if (i == 9) {
                    printf("Económico lleno. ¿Aceptar asiento en Primera Clase? (s/n) ");
                    scanf(" %c", &resp);
                    resp = tolower(resp);
                    if (resp == 's') {
                        for (int j = 0; j < asientos_p_c; j++) {
                            if (asientos[j] == 0) {
                                asientos[j] = 1;
                                imprimir(j + 1, 1);
                                break;
                            }
                        }
                    } else {
                        printf("El siguiente vuelo sale en 3 horas...\n");
                        break; 
                    }
                }
            }
        } else {
            printf("Opción no válida. Por favor, seleccione 1 o 2.\n");
        }
        
        printf("Desea agregar otro boleto? (s/n) ");
        scanf(" %c", &resp);
        resp = tolower(resp);
        if (resp != 's') {
            break; 
        }
    }

    return 0;
}

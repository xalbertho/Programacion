

#include <stdio.h>

#define NUM_SEATS 10
#define FIRST_CLASS_CAPACITY 5

// Función para mostrar el menú de opciones
void displayMenu() {
    printf("Por favor escriba 1 para 'Primera Clase'\n");
    printf("Por favor escriba 2 para 'Económico'\n");
}

// Función para mostrar el pase de abordaje
void printBoardingPass(int seatNumber, int isBusinessClass) {
    printf("----- PASE DE ABORDAJE -----\n");
    printf("Número de asiento: %d\n", seatNumber);
    if (isBusinessClass) {
        printf("Sección: Primera Clase\n");
    } else {
        printf("Sección: Económico\n");
    }
    printf("-----------------------------\n");
}

int main() {
    int seats[NUM_SEATS] = {0}; // Inicializamos todos los asientos como vacíos (0)
    int choice;
    
    while (1) {
        displayMenu();
        scanf("%d", &choice);
        
        if (choice == 1) { // Primera Clase
            for (int i = 0; i < FIRST_CLASS_CAPACITY; ++i) {
                if (seats[i] == 0) { // Si el asiento está vacío
                    seats[i] = 1; // Marcamos el asiento como ocupado
                    printBoardingPass(i + 1, 1); // Imprimimos el pase de abordaje
                    break;
                } else if (i == FIRST_CLASS_CAPACITY - 1) { // Si todos los asientos de primera clase están ocupados
                    printf("Primera clase llena. ¿Aceptar asiento en Económico? (1 = Sí, 0 = No): ");
                    int accept;
                    scanf("%d", &accept);
                    if (accept) {
                        for (int j = FIRST_CLASS_CAPACITY; j < NUM_SEATS; ++j) {
                            if (seats[j] == 0) { // Buscamos un asiento libre en la clase económica
                                seats[j] = 1; // Marcamos el asiento como ocupado
                                printBoardingPass(j + 1, 0); // Imprimimos el pase de abordaje
                                break;
                            }
                        }
                    } else {
                        printf("El próximo vuelo sale en 3 horas.\n");
                    }
                }
            }
        } else if (choice == 2) { // Económico
            for (int i = FIRST_CLASS_CAPACITY; i < NUM_SEATS; ++i) {
                if (seats[i] == 0) { // Si el asiento está vacío
                    seats[i] = 1; // Marcamos el asiento como ocupado
                    printBoardingPass(i + 1, 0); // Imprimimos el pase de abordaje
                    break;
                } else if (i == NUM_SEATS - 1) { // Si todos los asientos de clase económica están ocupados
                    printf("Clase económica llena. ¿Aceptar asiento en Primera Clase? (1 = Sí, 0 = No): ");
                    int accept;
                    scanf("%d", &accept);
                    if (accept) {
                        for (int j = 0; j < FIRST_CLASS_CAPACITY; ++j) {
                            if (seats[j] == 0) { // Buscamos un asiento libre en primera clase
                                seats[j] = 1; // Marcamos el asiento como ocupado
                                printBoardingPass(j + 1, 1); // Imprimimos el pase de abordaje
                                break;
                            }
                        }
                    } else {
                        printf("El próximo vuelo sale en 3 horas.\n");
                    }
                }
            }
        } else {
            printf("Opción no válida. Por favor, seleccione 1 o 2.\n");
        }
    }
    
    return 0;
}

/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-15
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>
#include<string.h>

void copiacadenas(char *destino, char *origen) {
    int i = 0;
    while(origen[i] != '\0') {
        destino[i] = origen[i];
        i++;
    }
    destino[i] = '\0';
}

int main()
{
    float saldo = 76.7;
    char info[100];
    sprintf(info, "Su saldo es: $%15.2f\n", saldo);
    printf("%s", info);

    return 0;
}

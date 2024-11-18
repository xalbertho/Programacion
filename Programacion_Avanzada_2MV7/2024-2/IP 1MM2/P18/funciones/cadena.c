/**
 * @file cadena.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-10
 * 
 * @copyright Copyright (c) 2024
 * 
 */


void copiar(char *origen, char *destino)
{
    int i = 0;
    while (origen[i] != '\0')
    {
        destino[i] = origen[i];
        i++;
    }
    destino[i] = '\0';
}

void concatena(char *cadena1, char *cadena2)
{
    int i = 0, j = 0;
    while (cadena1[i++] != '\0')
        ;
    i--;
    while (cadena2[j] != '\0')
    {
        cadena1[i] = cadena2[j];
        i++;
        j++;
    }
    cadena1[i] = '\0';
}

int tamanio(char *candena)
{
    int i = 0;
    while (candena[i++] != '\0');
    i--;
    return i;
}

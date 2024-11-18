/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-08
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    //char msj[] = "Hola";
    char msj[15];
    msj[0] = 'h';
    msj[1] = 'o';
    msj[2] = 'l';
    msj[3] = 'a';
    msj[4] = '\0';
    msj[5] = 'o';
    msj[6] = 'l';
    msj[7] = 'a';
    msj[8] = 'h';
    msj[9] = 'o';
    msj[10] = 'l';
    msj[11] = 'a';

    printf("%s", msj);
    return 0;
}

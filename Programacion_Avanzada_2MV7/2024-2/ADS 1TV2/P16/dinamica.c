/**
 * @file dinamica.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-30
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>
#include<stdlib.h>

struct Fecha{
    unsigned char _dia;
    unsigned char _mes;
    unsigned short _anio;
};



int main()
{
    int var =10;
    int *ptr = NULL;

    ptr = (int *)calloc(1, sizeof(int));
    
    printf("%p \n%i\n", ptr, *ptr);
    //ptr = (int *)malloc(100 * sizeof(int));
    *ptr = 88;

    ptr = (int *)realloc(ptr, 20000*sizeof(int));
    *(ptr+1) = 89;

    
    printf("%p \n%i\n", ptr, *ptr);

    free(ptr);
    
    return 0;
}


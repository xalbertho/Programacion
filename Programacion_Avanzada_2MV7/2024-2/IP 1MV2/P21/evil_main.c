/**
 * @file main2.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief MALLOC >:[
 * @version 0.1
 * @date 2024-04-16
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>
#include<stdlib.h>

int main()
{
    while(1000) {
        int *a = (int*)malloc(sizeof(int));
        *a = 10;
    }
    
    return 0;
}

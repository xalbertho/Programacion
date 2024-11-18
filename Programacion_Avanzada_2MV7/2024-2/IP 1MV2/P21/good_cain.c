/**
 * @file good_cain.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
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
    int *a = (int*)calloc(2, sizeof(int));
    printf("%i", *a);
    
    return 0;
}

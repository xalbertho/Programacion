/**
 * @file matriz1.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-22
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int (*m2)[3];
    m2 = malloc(9*sizeof(int));

    printf("%p - %p\n", *m2, *m2+1);

    return 0;
}

/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-16
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int a = 10;
    int *ptr;
    ptr = &a;

    printf("%i - %p\n%p - %i - %p\n", a, &a, ptr, *ptr, &ptr);
    return 0;
}

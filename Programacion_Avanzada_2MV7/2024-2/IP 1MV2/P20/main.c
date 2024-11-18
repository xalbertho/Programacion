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

int main()
{
    int a = 10;
    int arr[10];
    int m[2][2];
    arr[0] = 1;
    arr[1] = 2;

    printf("%p - %i", arr+1, *(arr+1));
    printf("%p - %i", arr+1, arr[1]);

    return 0;


    int *mc;
    mc = &a;

    printf("%i - %p\n%p - %i\n", a, &a, mc, *mc);
    
    return 0;
}

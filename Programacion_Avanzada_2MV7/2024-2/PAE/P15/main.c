/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-19
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int arr[3]= {1,6,50};

    printf("%p - %p - %p\n", arr, arr+1, arr+2);
    printf("%i - %i - %i\n", *(arr+0), *(arr+1), *(arr+2));
    printf("%i - %i - %i\n", arr[0], arr[1], arr[2]);
    return 0;
}

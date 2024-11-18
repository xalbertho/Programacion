/**
 * @file main2.c
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
    int arr[2] = {1,12};

    printf("%p - %i\n", arr+1, *(arr+1));
    printf("%p - %i\n", arr+1, arr[1]);
    
    return 0;
}

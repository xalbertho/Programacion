/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-17
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main()
{
    int a[3][3] = {{9,8,7},{6,5,4}, {3,2,1}};
    *(*a+4) = 15;
    *(*(a+1)+1) = 15;
    a[1][1] = 15;

    printf("%i - %p - %p\n", *(*a+4), a+1, a+2);
    
    return 0;
}

/**
 * @file malloc.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-22
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *arr = (int *)calloc(100, sizeof(int));

    arr[10] = 10;
    *(arr+10) = 10;

    
    return 0;
}

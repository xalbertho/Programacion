/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-18
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int *arr = (int *)malloc(100 * sizeof(int));

    printf("%p\n", arr);

    int *tmp = (int *)malloc(100000 * sizeof(int));
    memcpy(tmp, arr, 100 * sizeof(int));

    free(arr);
    arr = tmp;

    printf("%p\n", arr);

    return 0;
}

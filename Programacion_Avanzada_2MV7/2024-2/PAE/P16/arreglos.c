/**
 * @file arreglos.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-24
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int **arr;
    while (1)
    {
        arr = malloc(3 * sizeof(int *));

        arr[0] = (int *)malloc(3 * sizeof(int));
        arr[1] = (int *)malloc(5 * sizeof(int));
        arr[2] = (int *)malloc(10 * sizeof(int));

        free(*(arr+2));
        free(arr[1]);
        free(*(arr+0));
        free(arr);
    }

    return 0;
}

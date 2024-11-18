/**
 * @file realloc.c
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
    int *arr = (int *)malloc(5 * sizeof(int));

    arr[0] = 1;
    arr[1] = 2;
    arr[2] = 3;
    arr[3] = 4;
    arr[4] = 5;

    printf("%p\n", arr);
    //for (int i = 0; i < 5; i++)
    //{
    //    printf("%i ", *(arr + i));
    //}

    arr = realloc(arr, 100000*sizeof(int));
    printf("\n");

    printf("%p\n", arr);
    for (int i = 0; i < 10; i++)
    {
        printf("%i ", *(arr + i));
    }
    free(arr);
    return 0;
}

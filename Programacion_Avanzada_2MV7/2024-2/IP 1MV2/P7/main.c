/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-03-04
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main()
{
    int arrg[1000];

    srand(time(NULL));

    for (int i = 0; i < 1000; i++)
    {
        arrg[i] = (rand()%10000) + 1;
    }
    
    for (int i = 0; i < 1000; i++)
    {
        printf("%i\n", arrg[i]);
    }
    
    return 0;
}

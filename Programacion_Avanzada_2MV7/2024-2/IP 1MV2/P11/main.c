/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-03-19
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<stdio.h>

int main(int argc, char const *argv[])
{
    for (int i = 0; i < argc; i++)
    {
        if(argv[i][0] == '-' && argv[i][1] == 'h') {
            printf("\n\n\nAYUDAAAAAAA\n\n\n");
        } 
        //printf("%s\n", argv[i]);
    }
    
    return 0;
}

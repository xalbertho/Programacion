/**
 * @file fifo.c
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
    // Soy big-endian o little-endian?
    int entero = 0x12345678;
    int8_t *ptr;
    ptr = (int8_t *)(&entero);

    printf("%x\n", *ptr);
    printf("%x\n", *(ptr+1));
    printf("%x\n", *(ptr+2));
    printf("%x\n", *(ptr+3));

    return 0;
}

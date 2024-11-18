/**
 * @file biblioteca.h
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-03-27
 *
 * @copyright Copyright (c) 2024
 *
 */

void noDigitos(int numero, int *resultado)
{
    if (numero > 0)
    {
        (*resultado)++;
        numero /= 10;
        noDigitos(numero, resultado);
    }
}

void sumaDigitos(int numero, int *resultado)
{
    if (numero > 0)
    {
        (*resultado) += numero % 10;
        numero /= 10;
        sumaDigitos(numero, resultado);
    }
}

void ordena(int *arr, int n)
{
    int aux;
    for (int j = 0; j < n - 1; j++)
    {
        for (int i = 0; i < n - 1 - j; i++)
        {
            if (arr[i] > arr[i + 1])
            {
                aux = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = aux;
            }
        }
    }
}

void busquedaBinaria(int *arr, int inf, int sup, int x, int *res)
{
    int micha;
    if (inf <= sup)
    {
        micha = (inf + sup) / 2;
        if (x == arr[micha])
        {
            *res = micha;
            return;
        }
        else if (x < arr[micha])
        {
            sup = micha - 1;
        }
        else
        {
            inf = micha + 1;
        }
    }
    else
        return;
}

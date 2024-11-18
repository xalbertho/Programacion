/**
 * @brief 
 * 
 */





// Definicion

/**
 * @brief 
 * 
 * @param a 
 * @param b 
 * @return float 
 */
float suma(float a, float b)
{
    a = 8;
    b = 5;
    return a + b;
}

float sumaRef(float *a, float *b)
{
    *a = 20;
    *b = 6;
    return *a + *b;
}

void maizoro(float a, float b, float *suma, float *resta, float *mult, float *divi)
{
    *suma = a + b;
    *resta = a - b;
    *mult = a * b;
    *divi = a / b;
}

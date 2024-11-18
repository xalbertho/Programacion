
// Definiciones

float suma(float *a, float *b) {
    *a = 7.0f;
    *b = 6.0f;
    return *a+*b;
}

float sumaValor(float a, float b) {
    a = 7.0f;
    b = 6.0f;
    return a + b;
}

void maizoro(float a, float b, float *suma, float *resta, float *multi, float *divi) {
    *suma = a + b;
    *resta = a - b;
    *multi = a * b;
    *divi = a / b;
}
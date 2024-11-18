int suma(int a, int b)
{
    a = 7; 
    b = 25;
    return a + b;
}

int sumaRef(int *a, int *b) {
    *a = 7;
    *b = 25;
    return *a + *b;
}
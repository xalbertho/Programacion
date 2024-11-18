
#include <iostream>

using namespace std;
int hallar_max(int *,int);

int main(void)
{
    const int nElementos=5;
    int numeros[nElementos]={3,2,1,5,2};
    int numM=0;
    numM=hallar_max(numeros,nElementos);
    cout<<"El numero mallor es: "<<numM;

}

int hallar_max(int *dirvec, int nElementos)
{
  
    int max=*dirvec;

    for(int i=0; i<nElementos;i++)
    {
        if(*dirvec>max){
            max=*dirvec;
        }
        *dirvec++;
    }
    return max;
}
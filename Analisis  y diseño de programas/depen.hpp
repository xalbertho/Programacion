
#include <iostream>
#include <string>

using namespace std;

class Documento
{
private:
    string titulo;
    string cuerpo;
public:
    Documento(string,string);
    void muestra();
    ~Documento(){}
};

class Impresora
{
private:
    bool encendido;
public:
    Impresora(){};
    void Encender();
    void ImprimirDoc(Documento);

};




Documento::Documento(string a,string b)
{
    titulo=a;
    cuerpo=b;
}



void Documento::muestra()
{
    cout<<titulo;
    cout<<cuerpo;

}
Impresora::Impresora(){}
void Impresora::Encender()
{
    encendido=true;

}

void Impresora::ImprimirDoc(Documento a)
{
    if (encendido)
    {
        cout<<"Imprimiendo documento..."<<endl;
        a.muestra();
    }
    else
    cout<<"Impresora apagada"<<endl;

}
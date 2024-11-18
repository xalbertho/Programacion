
#include <iostream>

using namespace std;

class Boleto
{
protected:
float costob;
int asiento;

public:
    Boleto(int);
    void MuestraB();
};

class Hotel
{
    protected:
        float costoh;
        string tipo;
        
    public:
        Hotel(string);
        void MuestraH();  
};


class PlanV: public Boleto, public Hotel
{
    private:
        string destino;
        int duracion;
        float costo_viaje;

    public:
        PlanV(string, int,int,string);
        void imprimeCosto();
};

Boleto::Boleto(int a)
{
    asiento=a;
    if (asiento>10)
    {
        costob=650;
    }
    else
    {
        costob=1310;
    }
    
}


void Boleto::MuestraB()
{
    cout<<"El numero d asiento: "<<asiento<<endl;
    cout<<"El costo del boleto es: "<< costob <<endl;
}

Hotel::Hotel(string b)
{
    tipo=b;
    if(tipo=="Sencilla")
    {
        costoh=1218;
    }
    else
    {
        costoh=1950;
    }
    
}

void Hotel::MuestraH()
{
    cout<<"El costo de la habitacion es es: "<<costoh<<endl;
    cout<<"Tipo: "<<tipo;
}

PlanV::PlanV(string a, int b, int c, string d):Boleto(c),Hotel(d)
{
    destino=a;
    duracion=b;
    costo_viaje=0;

}

void PlanV::imprimeCosto()
{
    costo_viaje=duracion*costoh*costob;
    cout<<"Miles viajes\n";
    MuestraB();
    MuestraH();

    cout<<"Tu destino es: "<<destino;
    cout<<"El costo de tus vacaciones es: "<<costo_viaje;

}

#include "multiplicidad.hpp"

int main()
{
    Cliente cte(1234);
    Cuenta *cta=new Cuenta(7898,1231);

    cte.AgregarCuenta(cta);
    cta->Muestra();
}
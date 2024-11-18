#exception= detecta eventos que interrumpen la ejecucion de un programa

try:
    numerador=int(input("Ingrese el numero a dividir: "));
    denominador=int(input("Ingrese el numero a dividir: "));
    resultado=numerador/denominador;
except ZeroDivisionError:
    print("You can't divide by zero!!!");
except ValueError as e:
    print(e);
    print("Solo dividir entre numeros!! ");
except Exception as e:
    print(e)
    print("Algunas veces tenemos errores ");
else:
    print(resultado);
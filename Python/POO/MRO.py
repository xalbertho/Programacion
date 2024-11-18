'''
Metodo de resolucion de orden, actua en donde tenemos metodos llamados de la misma forma
pero tienen disntinto valor
en este caso veremos que metodo o atributo va a tener preferencia

'''

class A:
    def hablar(self):
        print("Hello everyone desde A");
class B(A):
    def hablar(self):
        print("Hello everyone desde B");
class C(A):
    def hablar(self):
        print("Hello everyone desde C");
class D(B,A):
    pass

'''
Por prioridad, primero se mostraria el de su misma clase, en  este caso D, despues tendra como prioridad
a las clases en el orden de las cuales fueron heredadas, aqui seria B,A respectivamente

        A       f
        |       |
        B       C
        \       /
            D
Este intendo de diagrama muestra la preferencia de los metodos, primero buscaria en la clase D por tener la preferenia
En caso de no tener el metodo, se iria con las clases padre de D, si primero le pasamos como argumento la clse B, esta tendra
preferencia, y en caso de no tener el metodo o atributo, se ira con la clase A.
Si nunguna de estas clases contiene el metodo, entonces empezara con C, que seria el segundo argumento que se le pasa a esta classe
y haria el mismo    proceso para encontrar el metodo o atributo deseado
'''
saludo=D()
saludo.hablar()
print(D.mro())
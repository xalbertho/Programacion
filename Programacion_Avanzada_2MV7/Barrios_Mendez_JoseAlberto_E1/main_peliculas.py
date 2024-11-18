import os
from modulo_catalogo import Catalogo,Pelicula


print("Bienvenido, se muestra el catalogo de ´peliculas asignado: \n")

lista=Catalogo()
peli1=Pelicula("Hallowen 1",1999,1.2,"Mayores de 15","Cristian nolan","Juan gabriel, martha suñiga","la pelicula trata sobre una persona que mataasi por gusto con un cuchillote")
lista.agregar(peli1)

peli2=Pelicula("Inseption",2010,"2 horas","Mayores 16","Cristopher nonal","Brad pit","Trata sobre personas que alteran la realidad a traves de los sueños")
lista.agregar(peli2)
lista.imprimir_catalogo()
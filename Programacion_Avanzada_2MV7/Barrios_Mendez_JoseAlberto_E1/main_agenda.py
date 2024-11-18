from modulo_agenda import Contacto,Agenda

listaa=Agenda()
contacto1=Contacto("Alberto",556093230)
contacto2=Contacto("Juan",34343443)

listaa.agregar(contacto1)
listaa.agregar(contacto2)

listaa.eliminar(contacto1)

print("Los contactos en la agenda son: ")
listaa.imprimir()

print("")
listaa.buscar_t(556093230)
listaa.buscar("Juan")


"""
NO USAR
"""
from multimethod import multimethod

class ClaseA:
    def habla(self):
        print("Que trancita por tus venas")
        
class ClaseB:
    def habla(self):
        print("Que pachuca por toluca")
        
class ClaseC:
    def habla(self):
        print("Que pdo paps")
        
class ClaseD(ClaseA, ClaseB, ClaseC):
    @multimethod
    def habla(self):
        print("Hola")
    
    @multimethod
    def habla(self, msj:str):
        print(msj)

morro = ClaseD()
morro.habla()
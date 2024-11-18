from abc import ABCMeta, abstractmethod

class Computadora(metaclass=ABCMeta):
    def __init__(self,memoria,procesador,almacenamiento,gpu):
        self._memoria=memoria
        self._procesador=procesador
        self._almacenamiento=almacenamiento
        self._gpu=gpu
    @property
    @abstractmethod
    def memoria(self):
        pass

    @property
    @abstractmethod
    def procesador(self):
        pass

    @property
    @abstractmethod
    def almacenamiento(self):
        pass

    @property
    @abstractmethod
    def gpu(self):
        pass

class Computadora_Portatil(Computadora):
    def __init__(self, memoria, procesador, almacenamiento, gpu,tamaño):
        super().__init__(memoria, procesador, almacenamiento, gpu)
        self._tamaño=tamaño

    @property
    def tamaño(self):
        return self._tamaño
    @tamaño.setter
    def tamaño(self,nuevo_tamaño):
        self._tamaño=nuevo_tamaño
    
    @property
    def memoria(self):
        return self._memoria

    @memoria.setter
    def memoria(self,nueva_memoria):
        self._memoria=nueva_memoria

    @property
    def procesador(self):
        return self._procesador
    @procesador.setter
    def procesador(self,nuevo_procesador):
        self._procesador=nuevo_procesador

    @property
    def almacenamiento(self):
        return self._almacenamiento

    @almacenamiento.setter
    def almacenamiento(self,nuevo_almacenamiento):
        self._almacenamiento=nuevo_almacenamiento

    @property
    def gpu(self):
        return self._gpu

    @gpu.setter
    def gpu(self,nueva_gpu):
        self._gpu=nueva_gpu

class Computadora_Esctritorio(Computadora):
    def __init__(self, memoria, procesador, almacenamiento, gpu,bocinas):
        super().__init__(memoria, procesador, almacenamiento, gpu)
        self._bocinas=bocinas

    @property
    def bocinas(self):
        return self._bocinas
    @bocinas.setter
    def bocinas(self,nueva_bocinas):
        self._bocinas=nueva_bocinas
        
    @property
    def memoria(self):
        return self._memoria

    @memoria.setter
    def memoria(self,nueva_memoria):
        self._memoria=nueva_memoria

    @property
    def procesador(self):
        return self._procesador
    @procesador.setter
    def procesador(self,nuevo_procesador):
        self._procesador=nuevo_procesador

    @property
    def almacenamiento(self):
        return self._almacenamiento

    @almacenamiento.setter
    def almacenamiento(self,nuevo_almacenamiento):
        self._almacenamiento=nuevo_almacenamiento

    @property
    def gpu(self):
        return self._gpu

    @gpu.setter
    def gpu(self,nueva_gpu):
        self._gpu=nueva_gpu
    
class TelefonoInteligente(Computadora):
    def __init__(self, memoria, procesador, almacenamiento, gpu,camara):
        super().__init__(memoria, procesador, almacenamiento, gpu)
        self._camara=camara

    @property
    def camara(self):
        return self._camara
    @camara.setter
    def camara(self,nueva_camara):
        self._camara=nueva_camara
        
    @property
    def memoria(self):
        return self._memoria

    @memoria.setter
    def memoria(self,nueva_memoria):
        self._memoria=nueva_memoria

    @property
    def procesador(self):
        return self._procesador
    @procesador.setter
    def procesador(self,nuevo_procesador):
        self._procesador=nuevo_procesador

    @property
    def almacenamiento(self):
        return self._almacenamiento

    @almacenamiento.setter
    def almacenamiento(self,nuevo_almacenamiento):
        self._almacenamiento=nuevo_almacenamiento

    @property
    def gpu(self):
        return self._gpu

    @gpu.setter
    def gpu(self,nueva_gpu):
        self._gpu=nueva_gpu
    
class Tablet(Computadora):
    def __init__(self, memoria, procesador, almacenamiento, gpu, pantalla):
        super().__init__(memoria, procesador, almacenamiento, gpu)
        self._pantalla=pantalla

    @property
    def pantalla(self):
        return self._pantalla
    @pantalla.setter
    def pantalla(self,nueva_pantalla):
        self._pantalla=nueva_pantalla

    @property
    def memoria(self):
        return self._memoria

    @memoria.setter
    def memoria(self,nueva_memoria):
        self._memoria=nueva_memoria

    @property
    def procesador(self):
        return self._procesador
    @procesador.setter
    def procesador(self,nuevo_procesador):
        self._procesador=nuevo_procesador

    @property
    def almacenamiento(self):
        return self._almacenamiento

    @almacenamiento.setter
    def almacenamiento(self,nuevo_almacenamiento):
        self._almacenamiento=nuevo_almacenamiento

    @property
    def gpu(self):
        return self._gpu

    @gpu.setter
    def gpu(self,nueva_gpu):
        self._gpu=nueva_gpu


          
lap1=Computadora_Portatil(memoria=32,procesador="i3 10th",almacenamiento=512,gpu="Nvidia",tamaño="12 pulagdas")
lap2=Computadora_Portatil(memoria=16,procesador="i7 11th",almacenamiento=1024,gpu="Nvidia 3050",tamaño="15 pulagdas")
lap3=Computadora_Portatil(memoria=64,procesador="ryzen 7560",almacenamiento=256,gpu="Nvidia 6018",tamaño="14 pulagdas")
pc1=Computadora_Esctritorio(memoria=16,procesador="i9 11th",almacenamiento=1024,gpu="Nvidia 4080",bocinas="bosse")
pc2=Computadora_Esctritorio(memoria=32,procesador="Pentium",almacenamiento=256,gpu="none",bocinas="akg")
pc3=Computadora_Esctritorio(memoria=16,procesador="i9 11th",almacenamiento=1024,gpu="Nvidia 4080",bocinas="bosse")
cel1=TelefonoInteligente(memoria=6,procesador="snapdragom 865",almacenamiento=64,gpu="sin datos",camara=24)
cel2=TelefonoInteligente(memoria=8,procesador="snapdragom gen 1",almacenamiento=512,gpu="grafic intel",camara=108)
cel3=TelefonoInteligente(memoria=4,procesador="A bionic 14",almacenamiento=64,gpu="sin datos",camara=12)
tab1=Tablet(memoria=6,procesador="A bionic 16",almacenamiento=512,gpu="apple grafics",pantalla=10.2)
tab2=Tablet(memoria=12,procesador="Kirin 980",almacenamiento=512,gpu="huawei graphics",pantalla=9)
tab3=Tablet(memoria=8,procesador="snapdragon 780",almacenamiento=256,gpu="sin datos",pantalla=8)

print("Objetos creados:")
print("Computadoras portátiles:")
print(f"Laptop 1: memoria={lap1.memoria}, procesador={lap1.procesador}, almacenamiento={lap1.almacenamiento}, gpu={lap1.gpu}, tamaño={lap1.tamaño}")
print(f"Laptop 2: memoria={lap2.memoria}, procesador={lap2.procesador}, almacenamiento={lap2.almacenamiento}, gpu={lap2.gpu}, tamaño={lap2.tamaño}")
print(f"Laptop 3: memoria={lap3.memoria}, procesador={lap3.procesador}, almacenamiento={lap3.almacenamiento}, gpu={lap3.gpu}, tamaño={lap3.tamaño}")

print("\nComputadoras de escritorio:")
print(f"PC 1: memoria={pc1.memoria}, procesador={pc1.procesador}, almacenamiento={pc1.almacenamiento}, gpu={pc1.gpu}, bocinas={pc1.bocinas}")
print(f"PC 2: memoria={pc2.memoria}, procesador={pc2.procesador}, almacenamiento={pc2.almacenamiento}, gpu={pc2.gpu}, bocinas={pc2.bocinas}")
print(f"PC 3: memoria={pc3.memoria}, procesador={pc3.procesador}, almacenamiento={pc3.almacenamiento}, gpu={pc3.gpu}, bocinas={pc3.bocinas}")

print("\nTeléfonos inteligentes:")
print(f"Celular 1: memoria={cel1.memoria}, procesador={cel1.procesador}, almacenamiento={cel1.almacenamiento}, gpu={cel1.gpu}, camara={cel1.camara}")
print(f"Celular 2: memoria={cel2.memoria}, procesador={cel2.procesador}, almacenamiento={cel2.almacenamiento}, gpu={cel2.gpu}, camara={cel2.camara}")
print(f"Celular 3: memoria={cel3.memoria}, procesador={cel3.procesador}, almacenamiento={cel3.almacenamiento}, gpu={cel3.gpu}, camara={cel3.camara}")

print("\nTabletas:")
print(f"Tablet 1: memoria={tab1.memoria}, procesador={tab1.procesador}, almacenamiento={tab1.almacenamiento}, gpu={tab1.gpu}, pantalla={tab1.pantalla}")
print(f"Tablet 2: memoria={tab2.memoria}, procesador={tab2.procesador}, almacenamiento={tab2.almacenamiento}, gpu={tab2.gpu}, pantalla={tab2.pantalla}")
print(f"Tablet 3: memoria={tab3.memoria}, procesador={tab3.procesador}, almacenamiento={tab3.almacenamiento}, gpu={tab3.gpu}, pantalla={tab3.pantalla}")
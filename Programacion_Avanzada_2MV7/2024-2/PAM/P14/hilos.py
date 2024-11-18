import threading
import time

def funcion(nombre):
    print(f"Inicio de hilo {nombre}")
    time.sleep(5)
    print(f"Fin de hilo {nombre}")
    
if __name__=="__main__":
    print("Inicio de hilo principal")
    hilo = threading.Thread(target=funcion, args=("1",))
    hilo.start()
    print("Fin de hilo principal")
    
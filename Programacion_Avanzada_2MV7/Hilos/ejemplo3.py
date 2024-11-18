import threading
import time

def funcion(nombre):
    print(f"Inicio de hilo {nombre}")
    time.sleep(5)
    print(f"Fin de hilo {nombre}")
    
if __name__=="__main__":
    print("Inicio de hilo principal")
    hilos = []
    for i in range(3):
        hilo = threading.Thread(target=funcion, args=(f"{i}",), daemon=True)
        hilo.start()
        hilos.append(hilo)
    
    for idx, hilo in enumerate(hilos):
        hilo.join()
    
    print("Fin de hilo principal")
import numpy as np
import matplotlib.pyplot as plt

# Cargar datos desde el archivo
data = np.loadtxt('senal_radar_DATA.dat')

# Separar los datos en tres columnas
tiempo = data[:, 0]
senal_emitida = data[:, 1]
senal_reflejada = data[:, 2]

# Graficar señal emitida
plt.figure()
plt.plot(tiempo, senal_emitida, 'b', linewidth=1.5)
plt.title('Señal Emitida')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.grid(True)

# Graficar señal reflejada
plt.figure()
plt.plot(tiempo, senal_reflejada, 'r', linewidth=1.5)
plt.title('Señal Reflejada')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.grid(True)

plt.show()

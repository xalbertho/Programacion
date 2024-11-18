import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('UV-Vis 4_12_2024 6_02 PM_240412182529_table.csv')

# Extraer la primera columna (valores del eje x)
x = df.iloc[:, 0]

# Graficar cada una de las otras columnas en función de la primera columna
for i in range(1, df.shape[1]):
    plt.plot(x, df.iloc[:, i], label=f'Columna {i}')

# Configurar el rango del eje x de 190 a 850
plt.xlim(190, 850)

# Configurar los intervalos del eje x para avanzar de 0.5
plt.xticks(range(190, 851, int(0.5 * (850 - 190))))

plt.xlabel('Etiqueta de la Primera Columna')
plt.ylabel('Valor')
plt.title('Resultados de la Prueba de Aplicación UV-Vis')
plt.legend()
plt.grid(True)
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos desde el archivo .csv
data = pd.read_csv('UV-Vis 4_12_2024 6_02 PM_240412182529_table.csv', header=2)

# Extraer los datos numéricos del DataFrame
data_matrix = data.iloc[:, 3:].values

# Extraer los valores de longitud de onda (primera fila)
wavelengths = data_matrix[0, :]

# Eliminar la primera fila de los datos
data_matrix = data_matrix[1:, :]

# Crear la figura y graficar los datos
fig, ax = plt.subplots()
for i in range(data_matrix.shape[0]):
    ax.plot(wavelengths, data_matrix[i, :], label=data.iloc[i+1, 2])
ax.set_xlabel('Longitud de onda')
ax.set_ylabel('Valor de la muestra')
ax.set_title('Datos de las muestras')
ax.legend()
plt.show()
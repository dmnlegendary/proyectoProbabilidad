import matplotlib.pyplot as plt

# Datos para el histograma
datos = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 6, 7, 7, 8]

# Crear el histograma
plt.hist(datos, bins=8, edgecolor='black')  # "bins" es el número de barras en el histograma

# Etiquetas y título
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Histograma de Datos')

# Mostrar el histograma
plt.show()

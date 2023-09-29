import matplotlib.pyplot as plt

# Función para leer los datos desde un archivo TXT
def leer_datos(archivo):
    try:
        with open(archivo, 'r') as file:
            lines = file.readlines()
            data = [line.strip().split(',') for line in lines]
            return data
    except FileNotFoundError:
        print("El archivo no existe.")
        return None

# Función para calcular la mediana
def calcular_mediana(datos):
    sorted_data = sorted(datos)
    n = len(sorted_data)
    if n % 2 == 0:
        median1 = sorted_data[n//2 - 1]
        median2 = sorted_data[n//2]
        return (median1 + median2) / 2
    else:
        return sorted_data[n//2]

# Función para calcular la media
def calcular_media(datos):
    n = len(datos)
    total = sum(datos)
    return total / n

# Función para calcular la varianza
def calcular_varianza(datos):
    n = len(datos)
    media = calcular_media(datos)
    suma = sum((x - media) ** 2 for x in datos)
    return suma / (n - 1)

# Función para calcular la moda
def calcular_moda(datos):
    counts = {}
    for x in datos:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    moda = [k for k, v in counts.items() if v == max(counts.values())]
    return moda

# Función para calcular la tabla de frecuencia
def calcular_tabla_frecuencia(datos):
    counts = {}
    n = len(datos)
    for x in datos:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    
    frecuencia = {}
    frecuencia_relativa = {}
    frecuencia_acumulada = 0
    tabla = []
    for k, v in sorted(counts.items()):
        frecuencia[k] = v
        frecuencia_relativa[k] = v / n
        frecuencia_acumulada += v / n
        tabla.append([k, v, v / n, frecuencia_acumulada])
    
    return tabla

# Función para calcular los cuartiles
def calcular_cuartiles(datos):
    sorted_data = sorted(datos)
    n = len(sorted_data)
    q1 = sorted_data[n // 4]
    q2 = sorted_data[n // 2]
    q3 = sorted_data[3 * n // 4]
    return q1, q2, q3

# Función para identificar puntos atípicos
def identificar_puntos_atipicos(datos):
    q1, q2, q3 = calcular_cuartiles(datos)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    atipicos = [x for x in datos if x < lower_bound or x > upper_bound]
    return atipicos

# Función para mostrar el diagrama de tallo y hoja
def mostrar_diagrama_tallo_hoja(datos):
    sorted_data = sorted(datos)
    stem_and_leaf = {}
    for x in sorted_data:
        stem = int(x // 10)
        leaf = int(x % 10)
        if stem in stem_and_leaf:
            stem_and_leaf[stem].append(leaf)
        else:
            stem_and_leaf[stem] = [leaf]
    
    for stem, leaves in sorted(stem_and_leaf.items()):
        leaves_str = ' '.join(map(str, sorted(leaves)))
        print(f"{stem} | {leaves_str}")

# Función para mostrar el histograma utilizando Matplotlib
def mostrar_histograma(datos):
    plt.hist(datos, bins=10, edgecolor='k')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.title('Histograma')
    plt.show()

# Función para mostrar la gráfica de caja utilizando Matplotlib
def mostrar_grafica_caja(datos):
    plt.boxplot(datos)
    plt.ylabel('Valores')
    plt.title('Gráfica de Caja')

    plt.show()

# Ejemplo de uso
if __name__ == "_main_":
    archivo = "E:\ESCOM\Materias\Probabilidad\cereals.txt"  # Reemplaza esto con el nombre de tu archivo
    datos = leer_datos(archivo)
    
    if datos:
        # Convierte los datos en una lista de números
        datos_numericos = [float(x) for x in datos[0]]
        
        print("Mediana:", calcular_mediana(datos_numericos))
        print("Media:", calcular_media(datos_numericos))
        print("Varianza:", calcular_varianza(datos_numericos))
        print("Moda:", calcular_moda(datos_numericos))
        
        tabla_frecuencia = calcular_tabla_frecuencia(datos_numericos)
        print("\nTabla de Frecuencia:")
        print("Valor | Frecuencia | Frecuencia Relativa | Frecuencia Acumulada")
        for fila in tabla_frecuencia:
            print(f"{fila[0]:5} | {fila[1]:10} | {fila[2]:18} | {fila[3]:20}")
        
        print("\nCuartiles:")
        q1, q2, q3 = calcular_cuartiles(datos_numericos)
        print("Q1:", q1)
        print("Q2 (Mediana):", q2)
        print("Q3:", q3)
        
        atipicos = identificar_puntos_atipicos(datos_numericos)
        if atipicos:
            print("\nPuntos Atípicos:")
            print(atipicos)
        else:
            print("\nNo hay puntos atípicos.")
        
        print("\nDiagrama de Tallo y Hoja:")
        mostrar_diagrama_tallo_hoja(datos_numericos)
        
        print("\nHistograma:")
        mostrar_histograma(datos_numericos)
        
        print("\nGráfica de Caja:")
        mostrar_grafica_caja(datos_numericos)
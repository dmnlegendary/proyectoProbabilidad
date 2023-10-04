# Leer los datos del archivo .txt
with open("cereals2reducido.txt") as file:
    lines = file.readlines()
    data = [[float(num) for num in line.strip().split(",")] for line in lines]

# Calcular la media de una lista de datos
def calculate_mean(data):
    n = len(data)
    total = sum(data)
    mean = total / n
    return mean

# Calcular la mediana de una lista de datos
def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        mid = n // 2
        median = (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        mid = n // 2
        median = sorted_data[mid]
    return median

# Calcular la moda de una lista de datos
def calculate_mode(data):
    counts = {}
    for num in data:
        counts[num] = counts.get(num, 0) + 1
    max_count = max(counts.values())
    mode = [num for num, count in counts.items() if count == max_count]
    return mode

# Calcular la varianza de una lista de datos
def calculate_variance(data):
    n = len(data)
    mean = calculate_mean(data)
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / (n - 1)
    return variance

# Calcular la desviación estándar de una lista de datos
def calculate_standard_deviation(data):
    variance = calculate_variance(data)
    standard_deviation = variance ** 0.5
    return standard_deviation

# Calcular la matriz de covarianza
def calcular_matriz_covarianza(data):
    # Calcula las medias de cada columna
    means = [sum(column) / len(column) for column in zip(*data)]

    # Calcula la matriz de covarianza
    cov_matrix = []
    for i in range(len(data[0])):
        row = []
        for j in range(len(data[0])):
            covariance = sum((data[k][i] - means[i]) * (data[k][j] - means[j]) for k in range(len(data))) / (len(data) - 1)
            row.append(covariance)
        cov_matrix.append(row)

    return cov_matrix

# Función para imprimir el diagrama de tallo y hoja
def print_stem_and_leaf_diagram(data):
    stem_leaf = {}
    for variable in data:
        for num in variable:
            stem, leaf = divmod(int(num), 10)
            if stem not in stem_leaf:
                stem_leaf[stem] = []
            stem_leaf[stem].append(leaf)
    for stem, leaves in sorted(stem_leaf.items()):
        leaves_str = ' '.join(str(leaf) for leaf in sorted(leaves))
        print(f"{stem} | {leaves_str}")

# Función para imprimir la tabla de frecuencias
def print_frequency_table(data):
    frequency_table = {}
    for variable in data:
        for num in variable:
            if num not in frequency_table:
                frequency_table[num] = 0
            frequency_table[num] += 1
    print("Valor\tFrecuencia")
    for value, frequency in sorted(frequency_table.items()):
        print(f"{value}\t{frequency}")

# Calcular y mostrar las estadísticas, diagrama de tallo y hoja, tabla de frecuencias y puntos atípicos para cada variable
for i, variable in enumerate(zip(*data)):
    print(f"Informacion para la variable {i + 1}:")
    variable = list(variable)
    print(f"Media: {calculate_mean(variable)}")
    print(f"Mediana: {calculate_median(variable)}")
    print(f"Moda: {calculate_mode(variable)}")
    print(f"Varianza: {calculate_variance(variable)}")
    print(f"Desviacion Estandar: {calculate_standard_deviation(variable)}")

    # Imprimir el diagrama de tallo y hoja
    print("Diagrama de tallo y hoja:")
    print_stem_and_leaf_diagram([variable])

    # Imprimir la tabla de frecuencias
    print("Tabla de frecuencias:")
    print_frequency_table([variable])

    # Calcular y mostrar los puntos atípicos
    outliers = []
    q1 = calculate_median(variable[:len(variable) // 2])
    q3 = calculate_median(variable[(len(variable) + 1) // 2:])
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    for num in variable:
        if num < lower_bound or num > upper_bound:
            if num < lower_bound:
                outliers.append(f"Extreme Low: {num}")
            else:
                outliers.append(f"Extreme High: {num}")
    print("Puntos atipicos:")
    if outliers:
        for outlier in outliers:
            print(outlier)
    else:
        print("No hay puntos atipicos.")

    print()

# Calcular y mostrar la matriz de covarianza
matriz_cov = calcular_matriz_covarianza(data)

print("Matriz de covarianza:")
for row in matriz_cov:
    print(row)
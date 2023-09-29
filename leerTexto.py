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

documento = "E:\\ESCOM\\Materias\\Probabilidad\\cereals.txt"

informacion = leer_datos(documento)

print(informacion)

'''
# Abre el archivo en modo lectura (por defecto)
with open(documento, 'r') as archivo:
    contenido = archivo.read()

# Imprime el contenido del archivo
print(contenido)
'''
import librerias

documento = "E:\\ESCOM\\Materias\\Probabilidad\\cereals2reducido.txt"

datos = librerias.leer_datos(documento)

if datos:
        # Convierte los datos en una lista de números
        datos_numericos = [float(x) for x in datos[0]]
        
        print("Mediana:", librerias.calcular_mediana(datos_numericos))
        print("Media:", librerias.calcular_media(datos_numericos))
        print("Varianza:", librerias.calcular_varianza(datos_numericos))
        print("Moda:", librerias.calcular_moda(datos_numericos))
        
        tabla_frecuencia = librerias.calcular_tabla_frecuencia(datos_numericos)
        print("\nTabla de Frecuencia:")
        print("Valor | Frecuencia | Frecuencia Relativa | Frecuencia Acumulada")
        for fila in tabla_frecuencia:
            print(f"{fila[0]:5} | {fila[1]:10} | {fila[2]:18} | {fila[3]:20}")
        
        print("\nCuartiles:")
        q1, q2, q3 = librerias.calcular_cuartiles(datos_numericos)
        print("Q1:", q1)
        print("Q2 (Mediana):", q2)
        print("Q3:", q3)
        
        atipicos = librerias.identificar_puntos_atipicos(datos_numericos)
        if atipicos:
            print("\nPuntos Atípicos:")
            print(atipicos)
        else:
            print("\nNo hay puntos atípicos.")
        
        print("\nDiagrama de Tallo y Hoja:")
        librerias.mostrar_diagrama_tallo_hoja(datos_numericos)
        
        print("\nHistograma:")
        librerias.mostrar_histograma(datos_numericos)
        
        print("\nGráfica de Caja:")
        librerias.mostrar_grafica_caja(datos_numericos)
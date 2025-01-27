"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """

    with open("files/input/data.csv", 'r') as file:
    # Leer el archivo CSV separado por espacios
        reader = csv.reader(file, delimiter='	')

        # Inicializar un diccionario para registrar las letras por cada valor de la segunda columna
        letras_por_valor = {}

        # Iterar sobre las filas del archivo CSV
        for row in reader:
            # Obtener el valor de la segunda columna
            valor = row[1]

            # Obtener la primera columna (letra) de la fila
            letra = row[0]

            # Agregar la letra a la lista correspondiente al valor en el diccionario
            if valor in letras_por_valor:
                letras_por_valor[valor].append(letra)
            else:
                letras_por_valor[valor] = [letra]

        # Convertir el diccionario en una lista de tuplas
        result = [(int(valor), letras) for valor, letras in letras_por_valor.items()]

        # Ordenar la lista de tuplas por la primera columna (valor)
        result.sort(key=lambda x: x[0])
        print(result)
        return result
    

pregunta_07()
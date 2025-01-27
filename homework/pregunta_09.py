"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    with open("files/input/data.csv", 'r') as file:
    # Leer el archivo CSV separado por espacios
        reader = csv.reader(file, delimiter='	')

        # Inicializar un diccionario para contar las apariciones de cada clave
        counts = {}

        # Iterar sobre las filas del archivo CSV
        for row in reader:
            # Obtener la clave de la columna 5
            dictionary = row[4]

            # Separar el diccionario en pares clave-valor
            pairs = dictionary.split(',')

            # Iterar sobre los pares clave-valor
            for pair in pairs:
                # Obtener la clave y el valor
                key, value = pair.split(':')

                # Incrementar la cantidad de apariciones de la clave en el diccionario
                counts[key] = counts.get(key, 0) + 1

        # Ordenar el diccionario alfabeticamente
        counts = dict(sorted(counts.items()))
    
    print(counts)
    return counts

pregunta_09()
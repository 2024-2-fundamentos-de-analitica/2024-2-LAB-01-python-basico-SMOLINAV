"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    with open("files/input/data.csv", 'r') as file:
    # Leer el archivo CSV separado por espacios
        reader = csv.reader(file, delimiter='	')

        # Inicializar una lista para almacenar las tuplas
        result = []

        # Iterar sobre las filas del archivo CSV
        for row in reader:
            # Obtener la letra de la primera columna
            letter = row[0]

            # Obtener la cantidad de elementos de las columnas 4 y 5
            count_4 = len(row[3].split(','))
            count_5 = len(row[4].split(','))

            # Agregar la tupla al resultado
            result.append((letter, count_4, count_5))

        print(result)
        return result
    
pregunta_10()
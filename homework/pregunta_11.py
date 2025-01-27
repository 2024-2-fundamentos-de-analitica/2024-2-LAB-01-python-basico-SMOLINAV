"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    with open("files/input/data.csv", 'r') as file:
    # Leer el archivo CSV separado por espacios
        reader = csv.reader(file, delimiter='	')

        # Inicializar un diccionario para contar la suma por cada letra
        sums = {}

        # Iterar sobre las filas del archivo CSV
        for row in reader:
            # Obtener la letra de la columna 4
            letter = row[3]

            letters = letter.split(',')

            # Obtener el valor de la columna 2
            value = int(row[1])

            # Sumar el valor al diccionario utilizando la letra como clave
            for l in letters:
                sums[l] = sums.get(l, 0) + value

        # Ordenar el diccionario por las claves
        sums = dict(sorted(sums.items()))
        print(sums)
        return sums
    
pregunta_11()
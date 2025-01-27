"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    with open("files/input/data.csv", 'r') as file:
    # Leer el archivo CSV separado por espacios
        reader = csv.reader(file, delimiter='	')

        # Inicializar un diccionario para contar la suma por cada letra
        sums = {}

        # Iterar sobre las filas del archivo CSV
        for row in reader:
            # Obtener la letra de la primera columna
            letter = row[0]

            # Obtener el valor de la columna 5
            datos = row[4].split(',')
            sum = 0
            for d in datos:
                sum += int(d.split(':')[1])

            # Sumar el valor al diccionario utilizando la letra como clave
            sums[letter] = sums.get(letter, 0) + sum
            sums = dict(sorted(sums.items()))
        
        print(sums)
        return sums
    
pregunta_12()
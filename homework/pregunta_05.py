"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    with open("files/input/data.csv", 'r') as file:
        lector_csv = csv.reader(file, delimiter='	')  # Usar espacio como delimitador

        # Contar cantidad de cada letra
        contar={}
        # Iterar sobre las filas del archivo CSV
        for row in lector_csv:
            # Obtener la primera columna (letra) de la fila
            letter = row[0]

            # Obtener la segunda columna de la fila
            suma = int(row[1])

            # Obtener el minimo y maximo de la segunda columna
            min_suma = min(contar.get(letter, (suma, suma))[0], suma)
            max_suma = max(contar.get(letter, (suma, suma))[1], suma)

            # Actualizar el diccionario con los valores minimos y maximos
            contar[letter] = (min_suma, max_suma)

        # Convertir el diccionario en una lista de tuplas
        resultado = [(letter, max_suma, min_suma) for letter, (min_suma, max_suma) in contar.items()]

        # Ordenar la lista de tuplas por la primera columna (letra)
        resultado.sort(key=lambda x: x[0])
        print(resultado)
    return resultado


pregunta_05()
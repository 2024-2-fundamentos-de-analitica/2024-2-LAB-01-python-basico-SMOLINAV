"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    with open("files/input/data.csv", 'r') as file:
        lector_csv = csv.reader(file, delimiter='	')  # Usar espacio como delimitador

        # Contar cantidad de cada letra
        contar = {}

        # Iterar sobre las filas del archivo CSV
        for row in lector_csv:
            # Obtener la primera columna (letra) de la fila
            letter = row[0]

            # Incrementar el contador de la letra en 1
            contar[letter] = contar.get(letter, 0) + 1

        # Convertir el diccionario en una lista de tuplas
        resultado = list(contar.items())

        # Ordenar la lista de tuplas por la primera columna (letra)
        resultado.sort(key=lambda x: x[0])

        # Imprimir la lista de tuplas
        print(resultado)

    return resultado


pregunta_02()
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """


    with open("files/input/data.csv", 'r') as file:
        lector_csv = csv.reader(file, delimiter='	')  # Usar espacio como delimitador

        suma = 0

        for fila in lector_csv:
            suma += int(fila[1])

        # Imprimir la suma
        print(suma)

    return suma


pregunta_01()
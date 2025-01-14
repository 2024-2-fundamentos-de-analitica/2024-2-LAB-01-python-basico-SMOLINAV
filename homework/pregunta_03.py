"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    with open("files/input/data.csv", 'r') as file:
        lector_csv = csv.reader(file, delimiter='	')  # Usar espacio como delimitador
        # Contar cantidad de cada letra
        contar = {}

        for row in lector_csv:  # Iterar sobre las filas del archivo CSV
            letter = row[0]  # Obtener la primera columna (letra) de la fila
            sum = int(row[1])  # Obtener la segunda columna (suma) de la fila
            contar[letter] = contar.get(letter, 0) + sum  # Incrementar el contador de la letra en la suma
        
        # Convertir el diccionario en una lista de tuplas
        resultado = list(contar.items())

        # Ordenar la lista de tuplas por la primera columna (letra)
        resultado.sort(key=lambda x: x[0])
        print(resultado)
    return resultado


pregunta_03()
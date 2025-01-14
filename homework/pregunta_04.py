"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """

    with open("files/input/data.csv", 'r') as file:
        lector_csv = csv.reader(file, delimiter='	')  # Usar espacio como delimitador

        # Contar cantidad de cada mes
        contar = {}  # Diccionario para contar la cantidad de cada mes

        for row in lector_csv:  # Iterar sobre las filas del archivo CSV
            date = row[2]  # Obtener la tercera columna (fecha) de la fila
            month = date.split('-')[1]  # Obtener el mes de la fecha
            contar[month] = contar.get(month, 0) + 1  # Incrementar el contador del mes en 1

        # Convertir el diccionario en una lista de tuplas
        resultado = list(contar.items())

        # Ordenar la lista de tuplas por la primera columna (mes)
        resultado.sort(key=lambda x: x[0])
        print(resultado)
    return resultado


pregunta_04()

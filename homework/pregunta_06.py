"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    with open("files/input/data.csv", 'r') as file:
    # Leer el archivo CSV separado por espacios
        lector_csv = csv.reader(file, delimiter='	')

        # Inicializar un diccionario para contar el menor y mayor valor por cada clave
        contar = {}

        # Iterar sobre las filas del archivo CSV
        for row in lector_csv:
            # Obtener la quinta columna (diccionario) de la fila
            dictionary = row[4]

            # Separar el diccionario en pares clave-valor
            pairs = dictionary.split(',')

            # Iterar sobre los pares clave-valor
            for pair in pairs:
                # Obtener la clave y el valor del par
                key, value = pair.split(':')

                # Convertir el valor a entero
                value = int(value)

                # Obtener el minimo y maximo de la clave
                min_value = min(contar.get(key, (value, value))[0], value)
                max_value = max(contar.get(key, (value, value))[1], value)

                # Actualizar el diccionario con los valores minimos y maximos
                contar[key] = (min_value, max_value)

        # Convertir el diccionario en una lista de tuplas
        resultado = [(key, min_value, max_value) for key, (min_value, max_value) in contar.items()]

        # Ordenar la lista de tuplas por la primera columna (clave)
        resultado.sort(key=lambda x: x[0])
        print(resultado)
    return resultado
    
pregunta_06()
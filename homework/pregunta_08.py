"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    with open("files/input/data.csv", 'r') as file:
    # Leer el archivo CSV separado por espacios
        reader = csv.reader(file, delimiter='	')

        # Inicializar un diccionario para registrar las letras por cada valor de la segunda columna
        letras_por_valor = {}

        # Iterar sobre las filas del archivo CSV
        for row in reader:
            # Obtener el valor de la segunda columna
            valor = row[1]

            # Obtener la primera columna (letra) de la fila
            letra = row[0]

            # Agregar la letra a la lista correspondiente al valor en el diccionario
            if valor in letras_por_valor:
                if letra in letras_por_valor[valor]:
                    continue
                else:
                    letras_por_valor[valor].append(letra)

            else:
                letras_por_valor[valor] = [letra]

        # Convertir el diccionario en una lista de tuplas
        result = [(int(valor), letras) for valor, letras in letras_por_valor.items()]

        # Ordenar la lista de tuplas por la primera columna (valor)
        result.sort(key=lambda x: x[0])

        # Ordenar la segunda parte de las tuplas alfabéticamente
        result = [(valor, sorted(letras)) for valor, letras in result]
        print(result)
        return result
    
pregunta_08()
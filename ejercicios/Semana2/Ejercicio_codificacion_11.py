"""
Práctica Operadores Asignación, Booleanos y Comparación
Objetivo

Comparador de Longitudes de Palabras

Instrucciones

El programa deberá tener una función personalizada llamada comparar_longitud que tome dos argumentos: palabra1 y palabra2.

Dentro de la función, utiliza operadores de asignación para almacenar la longitud de cada palabra en variables separadas, longitud1 y longitud2.

Compara las longitudes utilizando operadores de comparación. La función debe retornar un booleano: True si las longitudes son iguales, y False en caso contrario.

La función comparar_longitud debe hacer uso de la sentencia return para devolver el valor booleano resultante.

Fuera de la función, imprime un mensaje que muestre el resultado de la comparación.



Resultado esperado

¿Son "gato" y "perro" dos palabras con la misma longitud? False
"""

def comparar_longitud(palabra1, palabra2):
    """
    Compara las longitudes de dos palabras dadas y retorna un valor booleano.
 
    Args:
        palabra1 (str): La primera palabra para comparar.
        palabra2 (str): La segunda palabra para comparar.
 
    Returns:
        bool: True si ambas palabras tienen la misma longitud, False en caso contrario.
 
    """
    longitud1 = len(palabra1)
    longitud2 = len(palabra2)
 
    return longitud1 == longitud2
 
# Ejemplo de uso de la función
palabra1 = "gato"
palabra2 = "perro"
 
# Llamando a la función y almacenando el resultado
resultado = comparar_longitud(palabra1, palabra2)
 
# Imprimiendo el resultado
print('¿Son "gato" y "perro" dos palabras con la misma longitud?', resultado)


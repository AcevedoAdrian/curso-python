
"""
PRÁCTICA: FUNCIONES PROPIAS DE PYTHON
=====================================

OBJETIVO:
---------
Combinar el aprendizaje de funciones básicas de Python como print, len, str, int, 
float, y type con la creación de funciones personalizadas para profundizar en la 
comprensión y manipulación de tipos de datos básicos.

INSTRUCCIONES:
-------------

1. Función para contar caracteres en una cadena:
   * Define una función llamada 'contar_caracteres' que reciba un string como argumento.
   * Dentro de la función, usa len para determinar la longitud de la cadena.
   * Haz que la función imprima la cadena original y su longitud en el siguiente formato:
     "La frase 'Aprender Python es divertido' tiene 28 caracteres."
   * Llama a esta función con una frase de tu elección.

2. Función para convertir y mostrar tipos de números:
   * Crea una función 'convertir_numero' que tome un número entero como argumento.
   * Dentro de la función, convierte el número a cadena usando str y a flotante usando float.
   * Imprime el número en sus tres formas (entero, cadena y flotante) junto con su tipo 
     de dato (usando type) en el siguiente formato:
     
     Entero: 42, Tipo: <class 'int'>
     Cadena: 42, Tipo: <class 'str'>
     Flotante: 42.0, Tipo: <class 'float'>
     
   * Llama a esta función con un número entero de tu elección.

RESULTADO ESPERADO:
------------------
La frase 'Aprender Python es divertido' tiene 28 caracteres.

Entero: 42, Tipo: <class 'int'>
Cadena: 42, Tipo: <class 'str'>
Flotante: 42.0, Tipo: <class 'float'>
"""

def contar_caracteres(frase):
    """
    Funcion cuenta los caracteres de una frase.
    Imprime la frase y su longitud.

    Args:
        frase: La frase de la cual contar los caracteres.

    Returns:
        None
    """

    longitud = len(frase)
    print(f"La frase '{frase}' tiene {longitud} caracteres.")

contar_caracteres("Aprender Python es divertido")

def convertir_numero(numero):
    """
    Funcion convierte un numero entero a cadena y flotante.
    Imprime el numero en sus tres formas (entero, cadena y flotante) junto con su tipo de dato.

    Args:
        numero: El numero entero a convertir.

    Returns:
        None
    """

    cadena = str(numero)
    flotante = float(numero)
    print(f"Entero: {numero}, Tipo: {type(numero)}")
    print(f"Cadena: {cadena}, Tipo: {type(cadena)}")
    print(f"Flotante: {flotante}, Tipo: {type(flotante)}")

convertir_numero(42)

"""
Práctica Operadores Identidad, Pertenencia y Lógicos
Objetivo

Programar un juego de Adivinanza con Letras y Palabras. Este ejercicio tiene como objetivo que practiques con operadores de pertenencia, comparación y operadores lógicos en Python.



Instrucciones

Palabra a Adivinar: Al comienzo del programa, define una variable palabra_adivinar con un string que será la palabra que los usuarios deben adivinar.

Función adivinar_palabra: Escribe una función llamada adivinar_palabra. Esta función debe aceptar dos argumentos: letra_prueba y palabra_intento.

Verificar Letra en Palabra:

Utiliza operadores de pertenencia para comprobar si letra_prueba se encuentra en palabra_adivinar.

Almacena el resultado (True o False) en una variable letra_en_palabra.

Imprime el resultado con el formato: ¿La letra de prueba se encuentra en la palabra? [True/False].

Adivinar la Palabra:

Usa operadores de comparación para verificar si palabra_intento es igual a palabra_adivinar.

Combina la operación anterior con operadores lógicos y de comparación para verificar si palabra_intento tiene la misma longitud que palabra_adivinar.

Almacena el resultado en resultado_adivinanza.

Imprime el resultado con el formato: El jugador gana: [True/False].

Llamar a la Función:

Llama a la función y verifica su correcto funcionamiento proporcionándole como argumento una letra de prueba y una palabra de intento.



Resultado esperado

¿La letra de prueba se encuentra en la palabra? [True/False]

El jugador gana: [True/False]
"""

palabra_adivinar = "python"

def adivinar_palabra(letra_prueba, palabra_intento):
    """
    Determina si una letra está en una palabra específica y si un intento de palabra coincide con esa palabra.
 
    Args:
    letra_prueba (str): La letra a probar si está en la palabra.
    palabra_intento (str): La palabra intentada para adivinar la palabra correcta.
 
    Returns:
    None
    """
    letra_en_palabra = letra_prueba in palabra_adivinar
    print(f"¿La letra de prueba se encuentra en la palabra? {letra_en_palabra}")
    resultado_adivinanza = (palabra_intento == palabra_adivinar) and (len(palabra_intento) == len(palabra_adivinar))
    print(f"El jugador gana: {resultado_adivinanza}")

adivinar_palabra("p", "python")


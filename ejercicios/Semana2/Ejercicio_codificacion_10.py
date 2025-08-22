"""
Práctica Operadores Artiméticos
Objetivo

Crear un "Simulador de Calculadora de Calorías" utilizando operadores aritméticos en Python, integrando conocimientos previos sobre funciones, strings, y variables.



Instrucciones

Escribe un programa en Python que contenga una función llamada calcular_calorias. Esta función debe tomar tres argumentos: carbohidratos (cantidad en gramos), proteínas (cantidad en gramos) y grasas (cantidad en gramos).

Dentro de la función, utiliza operadores aritméticos para calcular las calorías totales, considerando que cada gramo de carbohidratos y proteínas aporta 4 calorías y cada gramo de grasas aporta 9 calorías.

La función debe devolver el total de calorías calculado.

Después de definir la función, realiza llamadas a calcular_calorias con diferentes cantidades de macronutrientes y muestra los resultados.

Como ejemplo se propone calcular las calorias de una comida con 10 gr de carbohidratos, 40 gr de proteínas y 5 gr de grasa.



Resultado esperado

Calorías totales: 245


"""
def calcular_calorias(carbohidratos, proteinas, grasas):
    """
    Función para calcular las calorías totales a partir de los macronutrientes. Retorna el total de calorías en gramos
    arg: 
      - carbohidratos: cantidad de carbohidratos en gramos
      - proteinas: cantidad de proteínas en gramos
      - grasas: cantidad de grasas en gramos
    return: 
      - total_calorias: total de calorías calculadas

    """
    calorias_carbohidratos = carbohidratos * 4
    calorias_proteinas = proteinas * 4
    calorias_grasas = grasas * 9
    
    total_calorias = calorias_carbohidratos + calorias_proteinas + calorias_grasas
    return total_calorias

print(calcular_calorias(10, 40, 5))
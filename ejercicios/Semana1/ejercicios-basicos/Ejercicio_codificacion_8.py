###
Práctica Sentencia return y Docstrings
Objetivo

Desarrollar un "Generador de Mensajes Personalizados" utilizando funciones en Python. El enfoque principal será en la sentencia return, la implementación de argumentos, el uso de strings y la incorporación de docstrings para la documentación de funciones.



Instrucciones

Escribe un programa en Python que contenga una función llamada generar_mensaje para crear mensajes personalizados.

Incluye un docstring al inicio de la función que describa su propósito, los parámetros que toma y lo que devuelve.

La función debe recibir dos argumentos:

nombre (argumento posicional). El nombre de una persona.

mensaje (parámetro con valor por defecto, "Bienvenido al curso de Python").

La función debe crear y devolver un mensaje completo utilizando la sentencia return, combinando el nombre y el mensaje predeterminado. Asegúrate de que el docstring refleje esta funcionalidad.

Después de definir la función, realiza una llamada a generar_mensaje con un nombre específico y muestra el resultado.



Resultado esperado

"¡Hola, Santiago! Bienvenido al curso de Python"




###


def  generar_mensaje(nombre, mensaje="Bienvenido al curso de Python"):
  """Genera un mensaje de saludo personalizado.

  Combina el nombre de una persona con un mensaje de bienvenida para crear
  un saludo personalizado. La función sigue el formato estándar de 
  "¡Hola, [nombre]! [mensaje]".

  Args:
      nombre: El nombre de la persona a saludar.
      mensaje: El mensaje a incluir en el saludo.
               Por defecto es "Bienvenido al curso de Python".

  Returns:
      Una cadena de texto formateada que contiene el nombre y el mensaje.
  """

  return f"¡Hola, {nombre}! {mensaje}"

print(generar_mensaje("Santiago", "Bienvenido al curso de Python"))

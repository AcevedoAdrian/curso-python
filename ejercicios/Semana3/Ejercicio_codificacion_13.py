'''
Práctica Listas
Objetivo

Programa un "Organizador de Biblioteca Personal" utilizando listas.



Instrucciones

El programa tendrá una función llamada aumentar_biblioteca que recibirá un argumento: nuevo_libro.

Dentro de la función aumentar_biblioteca se debe leer un listado de títulos de libros que el usuario ya ha leído. Esta lista se encuentra almacenada en un archivo de texto libros.txt que puedes consultar en el editor de código que aparece a la derecha. Para leer la lista de libros, sigue los siguientes pasos:

Para leer el archivo libros.txt utiliza la función por defecto open(). Investiga en este enlace el funcionamiento de esta función.

Convierte el archivo que acabas de leer a una lista utilizando la siguiente sentencia: libros = archivo.read().splitlines(). Más adelante en el curso entenderemos en detalle en consiste esta línea de código.

Termina la operación de lectura del archivo con la función archivo.close()

Dentro de la función, se debe añadir al final de la lista de libros el nuevo libro (nuevo_libro) especificado por el usuario.

La función debe devolver la lista completa de libros con el nuevo libro añadido.

El usuario debe mostrar por pantalla la lista completa de libros.

Adicionalmente, debe implementarse una nueva función llamada primer_libro_leido que imprimirá por pantalla el primer libro que el usuario ha leído y ha añadido a la lista de libros. Esta función recibirá como argumento la lista de libros y devolverá el primer libro de la lista.

El usuario debe mostrar por pantalla el primer libro de la lista.



Resultado esperado

La biblioteca de libros leídos es:

['Don Quijote de la Mancha', 'Orgullo y Prejuicio', 'Crimen y Castigo', 'Moby Dick', 'La Ilíada', 'El Gran Gatsby', 'Cien Años de Soledad', '1984', 'La Divina Comedia', 'Guerra y Paz', 'Las Aventuras de Huckleberry Finn']

El primer libro que he leído es: "Don Quijote de la Mancha"


'''

def aumentar_biblioteca(nuevo_libro):
    '''
    Aumenta la biblioteca personal con un nuevo libro.
    arg:
    nuevo_libro: str - El título del nuevo libro a añadir.
    return: list - La lista actualizada de libros.
    '''
    archivo = open("libros.txt", "r")
    libros = archivo.read().splitlines()
    archivo.close()
    libros += [nuevo_libro]
    return libros

def primer_libro_leido(libros):
    '''
    Devuelve el primer libro leído de la lista.
    arg:
    libros: list - La lista de libros leídos.
    return: str - El primer libro leído.
    '''
    if libros:
        return libros[0]
    return "No hay libros en la lista."

libros_actualizados = aumentar_biblioteca("Las Aventuras de Huckleberry Finn")

print("La biblioteca de libros leídos es:\n")
print(libros_actualizados)

print("El primer libro que he leído es:")
print(primer_libro_leido(libros_actualizados))
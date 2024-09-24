# Ejercicio: Análisis de Texto
# Crea un programa en Python que analice un texto proporcionado por el usuario y devuelva la siguiente información:

# Número total de palabras.
# Número total de caracteres (incluyendo espacios).
# Número de frases (considera una frase como un conjunto de palabras que termina en . ! o ?).
# Palabra más común (ignora las mayúsculas/minúsculas al contar).
# Longitud promedio de las palabras.

# Instrucciones:
# El programa debe pedir al usuario que ingrese un texto.
# Procesa el texto para calcular la información solicitada.
# Devuelve la información en un formato claro y fácil de leer

texto = input("Ingresa el texto a ser analizado ")

list_words = texto.split()[0] #para imprimir una sola palabra
num_words = len(texto.split())
num_characters_text = len(texto)

words = []
suma_words = 0

for i in range(0, num_words ,1):
    words.append(texto.split()[i])
    logitud = len(texto.split()[i])
    suma_words += logitud

# Este es un texto de ejemplo

print(f"Número total de palabras: {num_words}")
print(f"Número total de caracteres: {num_characters_text}")
# print(f"Número de frases: {}")
# print(f"palabra más común: {}")
print(f"Longitud promedio de las palabras: {suma_words/num_words}")
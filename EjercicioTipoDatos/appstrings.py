
#Propuesto strings, listas,diccionarios,tuples, sets
#Solicita al usuario un texto.
#Solicita también tres letras.
#Devuelve al usuario:
#El número de veces que aparecen esas letras, independientemente
#de en mayúsculas o minúsculas.
#Cuántas palabras hay en todo el texto.
#Cuál es la primera letra del texto y cuál es la última.
#Tenemos que mostrar el texto en orden inverso.
#El sistema nos dirá si la palabra ‘Pythonʼ aparece en el texto. Utiliza
#un diccionario para mostrar la respuesta al usuario.

texto = input("Introduce un texto: ")
letra1 = input("Introduce una letra: ")
letra2 = input("Introduce otra letra: ")
letra3 = input("Introduce otra letra: ")
texto = texto.lower()
letra1 = letra1.lower()
letra2 = letra2.lower()
letra3 = letra3.lower()
letras = [letra1, letra2, letra3]
letras_dict = {}
for letra in letras:
    letras_dict[letra] = texto.count(letra)
print(letras_dict)
palabras = texto.split()
print(f"El texto tiene {len(palabras)} palabras")
print(f"La primera letra del texto es {texto[0]} y la última es {texto[-1]}")
print(f"El texto en orden inverso es {texto[::-1]}")
if "python" in texto:
    print("La palabra 'Python' aparece en el texto")
else:
    print("La palabra 'Python' no aparece en el texto")

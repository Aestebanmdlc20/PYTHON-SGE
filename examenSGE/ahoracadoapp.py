import random

def leer_palabras_desde_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            return [linea.strip() for linea in archivo]
    except FileNotFoundError:
        palabras = ["python", "guitarra", "parapente", "computadora", "biblioteca", "cerveza"]
        with open(nombre_archivo, "w") as archivo:
            for palabra in palabras:
                archivo.write(palabra + "\n")
        return palabras

def obtener_palabra_secreta(palabras):
    return random.choice(palabras)

def mostrar_estado(letras_ocultas, intentos):
    print("Palabra: " + " ".join(letras_ocultas))
    print(f"Intentos restantes: {intentos}")

def actualizar_letras_ocultas(palabra_secreta, letras_ocultas, letra):
    for i, char in enumerate(palabra_secreta):
        if char == letra:
            letras_ocultas[i] = letra

def main():
    nombre_archivo = "palabras.txt"
    palabras = leer_palabras_desde_archivo(nombre_archivo)
    palabra_secreta = obtener_palabra_secreta(palabras)
    letras_ocultas = ["_" for _ in palabra_secreta]
    intentos = 6
    letras_correctas = set() # Uso el set para evitar letras duplicadas, es como el de java (collecion de valore unicos)

    print("Bienvenido al juego Ahorcado")
    mostrar_estado(letras_ocultas, intentos)

    while intentos > 0 and "_" in letras_ocultas:
        letra = input("Ingresa una letra: ").lower()
        if letra in letras_correctas:
            print("Ya ingresaste esta letra")
        elif letra in palabra_secreta:
            letras_correctas.add(letra)
            actualizar_letras_ocultas(palabra_secreta, letras_ocultas, letra)
        else:
            intentos -= 1
            print("Letra incorrecta")

        mostrar_estado(letras_ocultas, intentos)

    if "_" not in letras_ocultas:
        print("¡Felicidades! Has adivinado la palabra.")
    else:
        print(f"Has perdido. La palabra secreta era: {palabra_secreta}")

if __name__ == "__main__":
    main()
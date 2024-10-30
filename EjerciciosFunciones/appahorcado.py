"""
El programa elige una palabra secreta y le muestra al usuario los
guiones que se corresponden con las letras que tendrá el juego.
En cada intento, el jugador dirá una letra:
Si la letra está, se mostrará en los huecos en lugar de los guiones
Si no está, pierde una vida
Vamos a partir de 6 vidas e iremos descontando.
Si se agotan las vidas, el jugador pierde.
Si acierta la palabra, el jugador gana.
"""


def actualizar_palabra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra


def ahorcado(palabra_secreta):
    print("Bienvenido al juego del ahorcado")
    print("Tienes 6 vidas")
    vidas = 6
    palabra_mostrada = "_" * len(palabra_secreta)
    print(palabra_mostrada)
    while vidas > 0:
        letra = input("Introduce una letra: ")
        if letra in palabra_secreta:
            palabra_mostrada = actualizar_palabra(palabra_secreta, palabra_mostrada, letra)
            print(palabra_mostrada)
        else:
            vidas -= 1
            print(f"Has fallado. Te quedan {vidas} vidas")
        if palabra_mostrada == palabra_secreta:
            print("¡Has ganado!")
            break

ahorcado("hola")
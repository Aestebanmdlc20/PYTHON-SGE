"""
El programa le va a preguntar al usuario su nombre, y luego le va a decir
algo así como:
“Bueno, X, he pensado un número entre 1 y 100, y tienes solo ocho
intentos para adivinar cuál crees que es el número”.
Entonces, en cada intento el jugador dirá un número y el programa
puede responder cuatro cosas distintas:
Si el número que dijo el usuario es menor a 1 o superior a 100, le va
a decir que ha elegido un número que no está permitido.
Si el número que ha elegido el usuario es menor al que ha pensado
el programa, le va a decir que su respuesta es incorrecta y que ha
elegido un número menor al número secreto.
Si el usuario eligió un número mayor al número secreto, también se
lo hará saber de la misma manera.
Y si el usuario acertó el número secreto, se le va a informar que ha
ganado y cuántos intentos le ha tomado.
Si el usuario no ha acertado en este primer intento, se le va a volver a
pedir que elija otro
número. Y así hasta que gane o hasta que se agoten los ocho intentos.
"""

import random as rd

name = input("¿Cómo te llamas? ")
print(f"Hola, {name}, he pensado un número entre 1 y 100, tienes 8 intentos para adivinarlo.")
number = rd.randint(1, 100)
count = 0
acierto = False

while count < 8 and not acierto:
    count += 1
    guess = int(input("Introduce un número: "))
    if guess < 1 or guess > 100:
        print("El número debe estar entre 1 y 100.")
    elif guess < number:
        print("El número es mayor.")
    elif guess > number:
        print("El número es menor.")
    else:
        print(f"¡Has acertado! Enhorabuena, {name}.")
        print(f"Has acertado en {count} intentos.")
        acierto = True
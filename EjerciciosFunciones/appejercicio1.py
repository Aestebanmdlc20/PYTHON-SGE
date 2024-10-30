"""
Escribe una función que reciba un único parámetro numérico y devuelva
la suma de los números primos desde el 0 hasta dicho número incluído.
💡 El 0 y el 1 no se consideran primos.
"""

def es_primo(n):
    esPrimo = True
    if n < 2:
        esPrimo = False
    for i in range(2, n):
        if n % i == 0:
            esPrimo = False
    return esPrimo

def suma_primos(n):
    suma = 0
    for i in range(2, n+1):
        if es_primo(i):
            suma += i
    return suma

numero = 10
resultado = suma_primos(numero)
print(resultado)

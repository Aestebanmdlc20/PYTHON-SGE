import os

from Clases import Persona, Cliente

print("Bienvenido al banco, vamos a registrarte como cliente")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

persona = Persona(nombre, apellido)

cliente = Cliente(persona, 123456789, 0)
print(f"Enhorabuena {persona.nombre}, ya eres cliente del banco")

while True:
    os.system("cls")  # Limpio la consola

    print("¿Qué desea hacer?")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Salir")
    try:
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cliente.depositar(cantidad)
            print(f"Su balance actual es de {cliente.balance}")
        elif opcion == 2:
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cliente.retirar(cantidad)
            print(f"Su saldo actual es de {cliente.balance}")
        elif opcion == 3:
            print(f"Su balance es de: {cliente.balance} euros")
        elif opcion == 4:
            print("Gracias por usar nuestros servicios")
            break
        else:
            print("Opción no válida")
    except ValueError:
        print("Por favor, ingrese un número válido")
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cliente:
    def __init__(self, Persona, numero_cuenta, balance):
        self.persona = Persona
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"{self.persona} {self.numero_cuenta} {self.balance}"

    def depositar(self, cantidad):
        self.balance += cantidad

    def retirar(self, cantidad):
        if (self.balance - cantidad) >= 0:
            self.balance -= cantidad
        else:
            print("No tiene suficiente dinero")

    def consultar(self):
        return self.balance


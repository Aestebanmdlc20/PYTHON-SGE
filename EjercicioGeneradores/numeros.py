# numeros.py

def generador_turnos(area):
    contador = 1
    while True:
        yield f"{area} - {contador}"
        contador += 1

def mensaje_turno(func):
    def wrapper(*args, **kwargs):
        turno = func(*args, **kwargs)
        return f"Su turno es: {turno}. Espere a ser atendido."
    return wrapper
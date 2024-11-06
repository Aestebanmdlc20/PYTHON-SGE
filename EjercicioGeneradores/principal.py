# principal.py

from numeros import generador_turnos, mensaje_turno

# Inicializamos los generadores para cada área
generador_optica = generador_turnos("O")
generador_farmacia = generador_turnos("F")
generador_cosmetica = generador_turnos("C")

@mensaje_turno
def obtener_turno(area):
    if area == "Óptica":
        return next(generador_optica)
    elif area == "Farmacia":
        return next(generador_farmacia)
    elif area == "Cosmética":
        return next(generador_cosmetica)
    else:
        raise ValueError("Área no válida")

if __name__ == "__main__":
    area = input("Ingrese el área de atención (Óptica, Farmacia, Cosmética): ")
    try:
        print(obtener_turno(area))
    except ValueError as e:
        print(e)
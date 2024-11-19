import os

def bienvenida():
    print("Bienvenido al gestor de recetas")
    print("Las recetas se encuentran en la carpeta 'recetas'")

def contar_recetas():
    num_recetas = 0
    for root, dirs, files in os.walk('recetas'):
        num_recetas += len(files)
    print(f"Hay {num_recetas} recetas en la carpeta")

def mostrar_menu():
    print("\nMenú:")
    print("1. Leer receta")
    print("2. Crear receta")
    print("3. Crear categoría")
    print("4. Eliminar receta")
    print("5. Eliminar categoría")
    print("6. Finalizar programa")
    return input("Seleccione una opción: ")

def leer_receta():
    categoria = input("Ingrese la categoría: ")
    path = os.path.join('recetas', categoria)
    if os.path.exists(path):
        recetas = os.listdir(path)
        if recetas:
            print("Recetas disponibles:")
            for i, receta in enumerate(recetas):
                print(f"{i + 1}. {receta}")
            seleccion = int(input("Seleccione la receta a leer: ")) - 1
            with open(os.path.join(path, recetas[seleccion]), 'r') as file:
                print(file.read())
        else:
            print("No hay recetas en esta categoría.")
    else:
        print("La categoría no existe.")

def crear_receta():
    categoria = input("Ingrese la categoría: ")
    path = os.path.join('recetas', categoria)
    if os.path.exists(path):
        nombre = input("Ingrese el nombre de la receta: ") + '.txt'
        contenido = input("Ingrese el contenido de la receta: ")
        with open(os.path.join(path, nombre), 'w') as file:
            file.write(contenido)
        print("Receta creada con éxito.")
    else:
        print("La categoría no existe.")

def crear_categoria():
    nombre = input("Ingrese el nombre de la nueva categoría: ")
    path = os.path.join('recetas', nombre)
    if not os.path.exists(path):
        os.makedirs(path)
        print("Categoría creada con éxito.")
    else:
        print("La categoría ya existe.")

def eliminar_receta():
    categoria = input("Ingrese la categoria: ")
    path = os.path.join('recetas', categoria)
    if os.path.exists(path):
        recetas = os.listdir(path)
        if recetas:
            print("Recetas disponibles:")
            for i, receta in enumerate(recetas):
                print(f"{i + 1}. {receta}")
            seleccion = int(input("Seleccione la receta a eliminar: ")) - 1
            os.remove(os.path.join(path, recetas[seleccion]))
            print("Receta eliminada con éxito.")
        else:
            print("No hay recetas en esta categoria")
    else:
        print("La categoria no existe")

def eliminar_categoria():
    categoria = input("Ingrese la categoría a eliminar: ")
    path = os.path.join('recetas', categoria)
    if os.path.exists(path):
        os.rmdir(path)
        print("Categoría eliminada con exito")
    else:
        print("La categoria no existe")

def finalizar_programa():
    print("Finalizando programa...")
    exit()

def main():
    while True:
        bienvenida()
        contar_recetas()
        opcion = mostrar_menu()
        if opcion == '1':
            leer_receta()
        elif opcion == '2':
            crear_receta()
        elif opcion == '3':
            crear_categoria()
        elif opcion == '4':
            eliminar_receta()
        elif opcion == '5':
            eliminar_categoria()
        elif opcion == '6':
            finalizar_programa()
        else:
            print("Opción no válida.")
        input("Presione una tecla para continuar...")

if __name__ == "__main__":
    main()
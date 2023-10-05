from funciones_menu import *

print(" ")
print("Bienvenidos CRUD_DB clientes. ")
menu = {
    1: ingresar_registro,
    2: mostrar_datos,
    3: buscar_por_rut,
    4: eliminar_por_rut,
    5: actualizar_datos,
    6: None  # Deja esto como None para salir del bucle sin realizar ninguna operación adicional
}

while True:
    print("\nMenú:")
    print("1. Ingresar registro")
    print("2. Mostrar datos")
    print("3. Buscar por RUT")
    print("4. Eliminar por RUT")
    print("5. Actualizar datos")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    try:
        opcion = int(opcion)
        if opcion in menu:
            if menu[opcion] is None:
                print("Cerrando programa, y recuerda 'Todo esfuerzo es inútil si no crees en ti mismo'")
                break  # Salir del bucle del menú
            else:
                menu[opcion]()
        else:
            print("Opción no válida. Intente nuevamente.")
    except ValueError:
        print("Entrada no válida. Debe ingresar un número.")

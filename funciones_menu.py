
from persona import Persona
from validaciones import *
import json
from ruta import ruta_completa


registros = []

def ingresar_registro():
    while True:
        nombre_apellido = input("Ingrese el nombre y apellido del cliente: ")
        if not nombre_apellido:
            print("El nombre no puede estar vacío. Intente nuevamente.")
            continue

        # Verificar si el nombre y el apellido están separados por un espacio
        nombre_apellido_parts = nombre_apellido.split()
        if len(nombre_apellido_parts) != 2:
            print("Debe ingresar el nombre y el apellido separados por un espacio. Intente nuevamente.")
            continue

        nombre, apellido = nombre_apellido_parts

        # Verificar que el nombre y el apellido no contengan números o caracteres especiales
        if not nombre.isalpha() or not apellido.isalpha():
            print("El nombre y el apellido no pueden contener números o caracteres especiales. Intente nuevamente.")
            continue

        break  # Si todo está correcto, salir del bucle

    while True:
        rut = input("Ingrese el RUT del cliente (formato XX.XXX.XXX-X): ")
        if validar_rut(rut):
            break
        else:
            print("El RUT ingresado no tiene el formato correcto. Intente nuevamente.")

    while True:
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del cliente (formato dd/mm/yyyy): ")
        if validar_fecha_nacimiento(fecha_nacimiento):
            break
        else:
            print("La fecha de nacimiento no tiene el formato dd/mm/yyyy válido. Intente nuevamente.")

    while True:
        direccion = input("Ingrese la dirección del cliente: ")
        if not direccion:
            print("La dirección no puede estar vacía. Intente nuevamente.")
            continue
        elif validar_direccion(direccion):
            break
        else:
            print("La dirección no cumple con el formato válido. Intente nuevamente.")

    while True:
        telefono = input("Ingrese el número de teléfono del cliente (+569xxxxxxxx): ")
        telefono_formateado = formatear_telefono(telefono)
        if telefono_formateado:
            break

    while True:
        correo_electronico = input("Ingrese el correo electrónico del cliente (ejemplo@dominio.com): ")
        if validar_correo_electronico(correo_electronico):
            break
        else:
            print("El correo electrónico no tiene el formato válido. Intente nuevamente.")

    genero = input("Ingrese el género del cliente: ")
    estado_civil = input("Ingrese el estado civil del cliente: ")
    ocupacion = input("Ingrese la ocupación del cliente: ")
    informacion_adicional = input("Ingrese información adicional del cliente: ")

    # Una vez ingresados todos los valores, se crea la instancia de la clase
    persona = Persona(
        nombre_apellido,
        rut,
        fecha_nacimiento,
        direccion,
        telefono,
        correo_electronico,
        genero,
        estado_civil,
        ocupacion,
        informacion_adicional
    )

    # Agregar la instancia de la clase a la lista de registros
    registros.append(persona)
    print("Registro agregado exitosamente.")

    # Guardar la lista actualizada en formato JSON
    with open(ruta_completa, "w") as archivo_json:
        registros_json = [registro.to_dict() for registro in registros]
        json.dump(registros_json, archivo_json, indent=4)
        print("Registros guardados en registros.json.")

def mostrar_datos():
    if len(registros) == 0:
        print("No hay registros en la base de datos")
    else:
        for persona in registros:
            print(" ")
            print(persona)
            print(" ")

def buscar_por_rut():
    rut = input("Buscar por RUT (ejemplo: 15655455-5): ")
    for persona in registros:
        if persona.rut == rut:
            print("Registro encontrado:")
            print(persona)
            return
        else:
            print("No se encontró ningún registro con el RUT proporcionado")

def eliminar_por_rut():
    rut = input("Ingrese el RUT a eliminar: ")
    encontrado = False  # Bandera para verificar si se encontró el registro

    for persona in registros:
        if persona.rut == rut:
            registros.remove(persona)
            encontrado = True
            print("Registro eliminado exitosamente.")
            break  # Salir del bucle una vez que se haya eliminado el registro

    if not encontrado:
        print("No se encontró ningún registro con el RUT proporcionado.")
    else:
        # Guardar la lista actualizada en formato JSON
        with open(ruta_completa, "w") as archivo_json:
            registros_json = [registro.to_dict() for registro in registros]
            json.dump(registros_json, archivo_json, indent=4)
            print("Registro eliminado de Json")

def actualizar_datos():
    rut = input("Ingrese el rut del cliente que quiere actualizar: ")
    for persona in registros:
        if persona.rut == rut:
            print("Registro encontrado: ")
            print(persona)

            nombre_apellido = input("Ingrese el nuevo nombre y apellido del cliente: ")
            fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento del cliente (dd/mm/yyyy): ")
            direccion = input("Ingrese la nueva dirección del cliente: ")
            telefono = input("Ingrese el nuevo número de teléfono del cliente (+569xxxxxxxx): ")
            correo_electronico = input("Ingrese el nuevo correo electrónico del cliente (ejemplo@dominio.com): ")
            genero = input("Ingrese el nuevo género del cliente: ")
            estado_civil = input("Ingrese el nuevo estado civil del cliente: ")
            ocupacion = input("Ingrese la nueva ocupación del cliente: ")
            informacion_adicional = input("Ingrese nueva información adicional del cliente: ")

            # Actualizar los atributos de la persona
            persona.nombre_apellido = nombre_apellido
            persona.fecha_nacimiento = fecha_nacimiento
            persona.direccion = direccion
            persona.telefono = telefono
            persona.correo_electronico = correo_electronico
            persona.genero = genero
            persona.estado_civil = estado_civil
            persona.ocupacion = ocupacion
            persona.informacion_adicional = informacion_adicional
            
            print("Registro actualizado exitosamente.")

            # Guardar los registros actualizados en el archivo JSON
            with open(ruta_completa, "w") as archivo_json:
                registros_json = [registro.to_dict() for registro in registros]
                json.dump(registros_json, archivo_json, indent=4)
                
            return
    else:
        print("No se encontró ningún registro con el RUT proporcionado. ")
import re
import datetime

#Test validacion de rut segun formato.
def validar_rut(rut):
    patron = re.compile(r'^\d{1,2}\.\d{3}\.\d{3}[-][0-9kK]{1}$')
    return patron.match(rut) is not None



def validar_fecha_nacimiento(fecha):
    try:
        # Intenta convertir la fecha ingresada en un objeto de fecha
        fecha_obj = datetime.datetime.strptime(fecha, '%d/%m/%Y')
        return True
    except ValueError:
        return False
    

def validar_direccion(direccion):
    # Definir el patrón de dirección localmente en la función
    patron_direccion = re.compile(r'^[A-Za-z\s]+\s\d+$')
    
    # Verificar si la dirección coincide con el patrón local
    return bool(patron_direccion.match(direccion))


def validar_telefono(telefono):
    # Patrón para validar el formato de teléfono "+56912345678"
    patron_telefono = re.compile(r'^\+569\d{8}$')
    return bool(patron_telefono.match(telefono))

def formatear_telefono(telefono):
    # Formatea el número de teléfono en "+56912345678" si es válido
    if validar_telefono(telefono):
        return telefono
    else:
        print("El número de teléfono no tiene el formato válido. Se debe ingresar en el formato '+56912345678'.")
        return None
    

def validar_correo_electronico(correo_electronico):
    # Patrón para validar el formato del correo electrónico
    patron_correo = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    return bool(patron_correo.match(correo_electronico))
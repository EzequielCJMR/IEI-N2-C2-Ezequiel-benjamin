import re
from datetime import datetime

def validar_contrasena(contrasena):
    errores = []

    if len(contrasena) < 8 or len(contrasena) > 15:
        errores.append("La contraseña debe tener entre 8 y 15 caracteres.")

    if not any(c.isupper() for c in contrasena):
        errores.append("La contraseña debe contener al menos una letra mayúscula.")

    if not any(c.islower() for c in contrasena):
        errores.append("La contraseña debe contener al menos una letra minúscula.")

    if not any(c.isdigit() for c in contrasena):
        errores.append("La contraseña debe contener al menos un número.")

    if not any(c in "!@#$%&/" for c in contrasena):
        errores.append("La contraseña debe contener al menos uno de estos caracteres: !@#$%&/")

    return errores

def validar_correo(correo):
    # Patrón para validar que sea un correo electrónico real (ej: algo@dominio.com)
    patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(patron_correo, correo):
        return correo
    else:
        print('Correo Inválido, ingrese nuevamente...')
        return ''

def validar_fecha_nacimiento(fecha_nacimiento):
    # Patrón para validar formato dd/mm/aaaa
    patron_fecha = r'^\b(0[1-9]|[12]\d|3[01])[/](0[1-9]|1[0-2])[/](19\d\d|20\d\d)\b$'
    if re.match(patron_fecha, fecha_nacimiento):
        try:
            # Convierte el texto a un objeto de fecha de Python
            fecha = datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
            return fecha
        except ValueError:
            print('Fecha Inválida (día o mes no existen), ingrese nuevamente...')
            return ''
    else:
        print('Formato de fecha inválido, use dd/mm/aaaa...')
        return ''

def validar_genero(genero):
    # Solo permite las opciones 1, 2 o 3
    if genero in ['1', '2', '3']:
        return genero
    else:
        print('Género Inválido, ingrese un número del 1 al 3...')
        return ''
from datetime import date

from datos.repositorio.repo_encuesta import (
    listado_encuestas,
    listado_encuestas_publicadas,
    obtener_encuesta_id,
    guardar_encuesta,
    modificar_encuesta_bd,
    eliminar_encuesta_bd,
)


ESTADOS_VALIDOS = {"BORRADOR", "PUBLICADA", "CERRADA"}


def procesar_listado_encuestas():
    return listado_encuestas()

def obtener_encuesta_por_id(id_encuesta):
    return obtener_encuesta_id(id_encuesta)

def procesar_listado_encuestas_publicadas():
    return listado_encuestas_publicadas()


def crear_encuesta(titulo, descripcion, fecha_expiracion, estado, id_admin, id_categoria):
    titulo = titulo.strip()
    if not titulo:
        print("Error: El título de la encuesta es obligatorio.")
        return False
    if estado not in ESTADOS_VALIDOS:
        print("Error: Estado de encuesta inválido.")
        return False
    if fecha_expiracion and fecha_expiracion < date.today():
        print("Error: La fecha de expiración no puede ser anterior a hoy.")
        return False

    try:
        guardar_encuesta(
            titulo,
            descripcion.strip() or None,
            fecha_expiracion,
            estado,
            id_admin,
            id_categoria or None,
        )
        return True
    except Exception as error:
        print(f"Error al crear encuesta: {error}")
        return False


def modificar_encuesta(encuesta, titulo, descripcion, fecha_expiracion, estado, id_categoria):
    if titulo:
        encuesta.titulo = titulo
    if descripcion:
        encuesta.descripcion = descripcion
    if fecha_expiracion:
        if fecha_expiracion < date.today():
            print("Error: La fecha de expiración no puede ser anterior a hoy.")
            return False
        encuesta.fecha_expiracion = fecha_expiracion
    if estado:
        estado = estado.upper()
        if estado not in ESTADOS_VALIDOS:
            print("Error: Estado de encuesta inválido.")
            return False
        encuesta.estado = estado
    if id_categoria:
        encuesta.id_categoria = id_categoria

    try:
        return modificar_encuesta_bd(
            encuesta,
            titulo,
            descripcion,
            fecha_expiracion,
            estado,
            id_categoria,
        ) is not None
    except Exception as error:
        print(f"Error al modificar encuesta: {error}")
        return False


def eliminar_encuesta(encuesta):
    try:
        return eliminar_encuesta_bd(encuesta)
    except Exception as error:
        print(f"Error al eliminar encuesta: {error}")
        return False

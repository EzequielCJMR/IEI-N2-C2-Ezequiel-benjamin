from datos.modelos.Encuesta import Encuesta


def listado_encuestas():
    return Encuesta.select().order_by(Encuesta.id_encuesta)


def listado_encuestas_publicadas():
    return Encuesta.select().where(Encuesta.estado == "PUBLICADA")


def obtener_encuesta_id(id_encuesta):
    return Encuesta.get_or_none(Encuesta.id_encuesta == id_encuesta)

def guardar_encuesta(titulo, descripcion, fecha_expiracion, estado, id_admin, id_categoria):
    return Encuesta.create(
        titulo=titulo,
        descripcion=descripcion,
        fecha_expiracion=fecha_expiracion,
        estado=estado,
        id_admin=id_admin,
        id_categoria=id_categoria,
    )

def modificar_encuesta_bd(encuesta, titulo=None, descripcion=None, fecha_expiracion=None, estado=None, id_categoria=None):
    if titulo:
        encuesta.titulo = titulo
    if descripcion:
        encuesta.descripcion = descripcion
    if fecha_expiracion:
        encuesta.fecha_expiracion = fecha_expiracion
    if estado:
        encuesta.estado = estado
    if id_categoria:
        encuesta.id_categoria = id_categoria
    encuesta.save()
    return encuesta

def eliminar_encuesta_bd(encuesta):
    encuesta.delete_instance()
    return True

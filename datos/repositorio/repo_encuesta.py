from datos.modelos.Encuesta import Encuesta


def listado_encuestas():
    return Encuesta.select().order_by(Encuesta.id_encuesta)


def listado_encuestas_publicadas():
    return Encuesta.select().where(Encuesta.estado == "PUBLICADA")


def obtener_encuesta_id(id_encuesta):
    return Encuesta.get_or_none(Encuesta.id_encuesta == id_encuesta)

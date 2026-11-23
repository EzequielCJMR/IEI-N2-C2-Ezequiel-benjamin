from datos.modelos.categoria import Categoria


def listado_categorias():
    return Categoria.select().order_by(Categoria.nombre)


def obtener_categoria_id(id_categoria):
    return Categoria.get_or_none(Categoria.id_categoria == id_categoria)


def obtener_categoria_nombre(nombre):
    return Categoria.get_or_none(Categoria.nombre == nombre)

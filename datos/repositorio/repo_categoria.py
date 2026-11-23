from datos.modelos.categoria import Categoria


def listado_categorias():
    return Categoria.select().order_by(Categoria.nombre)


def obtener_categoria_id(id_categoria):
    return Categoria.get_or_none(Categoria.id_categoria == id_categoria)


def obtener_categoria_nombre(nombre):
    return Categoria.get_or_none(Categoria.nombre == nombre)

def guardar_categoria(nombre, descripcion=None):
    try:
        return Categoria.create(nombre=nombre, descripcion=descripcion)
    except Exception:
        return None

def modificar_categoria_bd(categoria, nombre=None, descripcion=None):
    if nombre:
        categoria.nombre = nombre
    if descripcion:
        categoria.descripcion = descripcion
    categoria.save()
    return categoria

def eliminar_categoria_bd(categoria):
    categoria.delete_instance()
    return True

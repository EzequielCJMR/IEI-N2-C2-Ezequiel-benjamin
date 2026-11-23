from datos.modelos.categoria import Categoria
from datos.repositorio.repo_categoria import obtener_categoria_nombre


def procesar_listado_categorias():
    return Categoria.select().order_by(Categoria.nombre)


def crear_categoria(nombre, descripcion):
    nombre = nombre.strip()
    descripcion = descripcion.strip()

    if not nombre:
        print("Error: El nombre de la categoría es obligatorio.")
        return False
    if obtener_categoria_nombre(nombre):
        print("Error: Ya existe una categoría con ese nombre.")
        return False

    try:
        Categoria.create(nombre=nombre, descripcion=descripcion or None)
        return True
    except Exception as error:
        print(f"Error al crear categoría: {error}")
        return False


def modificar_categoria(categoria, nombre, descripcion):
    nombre = nombre.strip()
    descripcion = descripcion.strip()

    if nombre:
        repetida = obtener_categoria_nombre(nombre)
        if repetida and repetida.id_categoria != categoria.id_categoria:
            print("Error: Ya existe una categoría con ese nombre.")
            return False
        categoria.nombre = nombre
    if descripcion:
        categoria.descripcion = descripcion

    try:
        categoria.save()
        return True
    except Exception as error:
        print(f"Error al modificar categoría: {error}")
        return False


def eliminar_categoria(categoria):
    try:
        categoria.delete_instance()
        return True
    except Exception as error:
        print(f"Error al eliminar categoría: {error}")
        return False

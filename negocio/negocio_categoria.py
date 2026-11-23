from datos.repositorio.repo_categoria import (
    listado_categorias,
    obtener_categoria_id,
    obtener_categoria_nombre,
    guardar_categoria,
    modificar_categoria_bd,
    eliminar_categoria_bd,
)


def procesar_listado_categorias():
    return listado_categorias()

def obtener_categoria_por_id(id_categoria):
    return obtener_categoria_id(id_categoria)


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
        return guardar_categoria(nombre, descripcion or None) is not None
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
        return modificar_categoria_bd(categoria, nombre, descripcion) is not None
    except Exception as error:
        print(f"Error al modificar categoría: {error}")
        return False


def eliminar_categoria(categoria):
    try:
        return eliminar_categoria_bd(categoria)
    except Exception as error:
        print(f"Error al eliminar categoría: {error}")
        return False

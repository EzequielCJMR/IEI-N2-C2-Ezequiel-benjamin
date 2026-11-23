from datos.repositorio.repo_categoria import obtener_categoria_id
from negocio.negocio_categoria import (
    procesar_listado_categorias,
    crear_categoria,
    modificar_categoria,
    eliminar_categoria,
)


def mostrar_listado_categorias():
    categorias = procesar_listado_categorias()
    print("\n--- LISTADO DE CATEGORÍAS ---")
    if not categorias:
        print("No hay categorías registradas.")
        return
    for categoria in categorias:
        print(
            f"ID: {categoria.id_categoria} | "
            f"Nombre: {categoria.nombre} | "
            f"Descripción: {categoria.descripcion or '-'}"
        )
    print("-----------------------------\n")


def ingresar_categoria():
    nombre = input("Nombre de la categoría: ").strip()
    descripcion = input("Descripción: ").strip()
    if crear_categoria(nombre, descripcion):
        print("Categoría creada correctamente.")


def modificar_categoria_presentacion():
    try:
        id_categoria = int(input("ID de la categoría: ").strip())
    except ValueError:
        print("Error: El ID debe ser numérico.")
        return

    categoria = obtener_categoria_id(id_categoria)
    if not categoria:
        print("No existe una categoría con ese ID.")
        return

    nombre = input(f"Nuevo nombre (actual: {categoria.nombre}): ").strip()
    descripcion = input(
        f"Nueva descripción (actual: {categoria.descripcion or '-'}): "
    ).strip()
    if modificar_categoria(categoria, nombre, descripcion):
        print("Categoría modificada correctamente.")


def eliminar_categoria_presentacion():
    try:
        id_categoria = int(input("ID de la categoría a eliminar: ").strip())
    except ValueError:
        print("Error: El ID debe ser numérico.")
        return

    categoria = obtener_categoria_id(id_categoria)
    if not categoria:
        print("No existe una categoría con ese ID.")
        return
    if eliminar_categoria(categoria):
        print("Categoría eliminada correctamente.")

from datetime import datetime

from negocio.negocio_encuesta import (
    procesar_listado_encuestas,
    crear_encuesta,
    modificar_encuesta,
    eliminar_encuesta,
    obtener_encuesta_por_id,
)
from negocio.negocio_administrador import procesar_listado_administradores
from negocio.negocio_categoria import procesar_listado_categorias


def _leer_fecha(texto):
    valor = input(texto).strip()
    if not valor:
        return None
    try:
        return datetime.strptime(valor, "%Y-%m-%d").date()
    except ValueError:
        print("Error: Formato de fecha incorrecto. Usa YYYY-MM-DD.")
        return ""


def mostrar_listado_encuestas():
    encuestas = procesar_listado_encuestas()
    print("\n--- LISTADO DE ENCUESTAS ---")
    if not encuestas:
        print("No hay encuestas registradas.")
        return
    for encuesta in encuestas:
        print(
            f"ID: {encuesta.id_encuesta} | "
            f"Título: {encuesta.titulo} | "
            f"Estado: {encuesta.estado} | "
            f"Expira: {encuesta.fecha_expiracion or '-'}"
        )
    print("-----------------------------\n")


def ingresar_encuesta():
    titulo = input("Título: ").strip()
    descripcion = input("Descripción: ").strip()
    fecha_expiracion = _leer_fecha("Fecha de expiración (YYYY-MM-DD, opcional): ")
    if fecha_expiracion == "":
        return

    estado = input("Estado (BORRADOR/PUBLICADA/CERRADA): ").strip().upper()

    administradores = procesar_listado_administradores()
    if not administradores:
        print("No hay administradores registrados.")
        return
    print("Administradores:")
    for administrador in administradores:
        print(
            f"ID Usuario: {administrador.id_usuario} | "
            f"Cargo: {administrador.cargo}"
        )
    try:
        id_admin = int(input("ID del administrador: ").strip())
    except ValueError:
        print("Error: El ID debe ser numérico.")
        return

    categorias = procesar_listado_categorias()
    if categorias:
        print("Categorías:")
        for categoria in categorias:
            print(f"ID: {categoria.id_categoria} | {categoria.nombre}")
    try:
        id_categoria = input("ID de categoría (opcional): ").strip()
        id_categoria = int(id_categoria) if id_categoria else None
    except ValueError:
        print("Error: El ID de categoría debe ser numérico.")
        return

    if crear_encuesta(
        titulo,
        descripcion,
        fecha_expiracion,
        estado,
        id_admin,
        id_categoria,
    ):
        print("Encuesta creada correctamente.")


def modificar_encuesta_presentacion():
    try:
        id_encuesta = int(input("ID de la encuesta: ").strip())
    except ValueError:
        print("Error: El ID debe ser numérico.")
        return

    encuesta = obtener_encuesta_por_id(id_encuesta)
    if not encuesta:
        print("No existe una encuesta con ese ID.")
        return

    titulo = input(f"Nuevo título (actual: {encuesta.titulo}): ").strip()
    descripcion = input(
        f"Nueva descripción (actual: {encuesta.descripcion or '-'}): "
    ).strip()
    fecha_expiracion = _leer_fecha(
        f"Nueva fecha de expiración (actual: {encuesta.fecha_expiracion or '-'}, YYYY-MM-DD): "
    )
    if fecha_expiracion == "":
        return
    estado = input(
        f"Nuevo estado (actual: {encuesta.estado}): "
    ).strip().upper()
    id_categoria_texto = input(
        f"Nueva categoría (actual: {encuesta.id_categoria or '-'}): "
    ).strip()
    try:
        id_categoria = int(id_categoria_texto) if id_categoria_texto else None
    except ValueError:
        print("Error: El ID de categoría debe ser numérico.")
        return

    if modificar_encuesta(
        encuesta,
        titulo,
        descripcion,
        fecha_expiracion,
        estado,
        id_categoria,
    ):
        print("Encuesta modificada correctamente.")


def eliminar_encuesta_presentacion():
    try:
        id_encuesta = int(input("ID de la encuesta a eliminar: ").strip())
    except ValueError:
        print("Error: El ID debe ser numérico.")
        return

    encuesta = obtener_encuesta_por_id(id_encuesta)
    if not encuesta:
        print("No existe una encuesta con ese ID.")
        return
    if eliminar_encuesta(encuesta):
        print("Encuesta eliminada correctamente.")

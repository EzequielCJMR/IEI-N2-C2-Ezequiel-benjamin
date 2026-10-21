from datos.modelos.usuario import Usuario
from negocio.negocio_usuarios import (
    procesar_listado_usuarios, 
    crear_objeto_usuario, 
    modificar_objeto_usuario
)
from datos.repositorio.repo_usuarios import obtener_usuario_id, eliminar_usuario_bd

def mostrar_listado_usuarios():
    print("\n--- LISTADO DE USUARIOS ---")
    usuarios = procesar_listado_usuarios()
    
    if not usuarios:
        print("No hay usuarios registrados.")
        return

    for user in usuarios:
        print(f"ID: {user.id_usuario} | Nombre: {user.nombre} | Email: {user.email} | RUT: {user.rut} | Rol: {user.rol}")
    print("---------------------------\n")

def ingresar_usuario():
    print("\n--- INGRESAR USUARIO ---")
    nombre = input("Nombre: ").strip()
    rut = input("RUT: ").strip()
    email = input("Email: ").strip()
    contrasena = input("Contraseña: ").strip()
    rol = input("Rol: ").strip()

    # Llamamos al negocio (que a su vez llamará al repositorio)
    if crear_objeto_usuario(nombre, rut, email, contrasena, rol):
        print("¡Usuario guardado con éxito!")

def modificar_usuario():
    print("\n--- MODIFICAR USUARIO ---")
    try:
        id_usuario = int(input("ID del usuario a modificar: ").strip())
    except ValueError:
        print("Error: El ID debe ser un número.")
        return

    user = obtener_usuario_id(id_usuario)
    if not user:
        print("Error: No existe un usuario con ese ID.")
        return

    nombre = input(f"Nuevo Nombre (actual: {user.nombre}): ").strip()
    email = input(f"Nuevo Email (actual: {user.email}): ").strip()
    contrasena = input(f"Nueva Contraseña (actual: {user.contrasena}): ").strip()
    rol = input(f"Nuevo Rol (actual: {user.rol}): ").strip()

    if modificar_objeto_usuario(user, nombre, email, contrasena, rol):
        print("¡Usuario modificado con éxito!")

def eliminar_usuario():
    print("\n--- ELIMINAR USUARIO ---")
    try:
        id_usuario = int(input("ID del usuario a eliminar: ").strip())
    except ValueError:
        print("Error: El ID debe ser un número.")
        return

    user = obtener_usuario_id(id_usuario)
    if not user:
        print("Error: No existe un usuario con ese ID.")
        return

    if eliminar_usuario_bd(user):
        print("¡Usuario eliminado con éxito!")
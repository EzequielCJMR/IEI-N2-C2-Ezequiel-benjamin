from datetime import datetime
from datos.modelos.encuestado import Encuestado
from datos.modelos.usuario import Usuario
from negocio.negocio_encuestado import (
    crear_encuestado_completo, 
    procesar_listado_encuestados,
    modificar_encuestado_completo  # <-- AGREGADO
)
from datos.repositorio.repo_encuestado import obtener_encuestado_id, eliminar_encuestado_bd

def mostrar_listado_encuestados():
    encuestados = procesar_listado_encuestados()
    print("\n--- LISTADO DE ENCUESTADOS ---")
    if not encuestados:
        print("No hay encuestados registrados.")
        return
        
    for enc in encuestados:
        # Buscamos el nombre del usuario para que se vea mejor
        user = Usuario.get_or_none(Usuario.id_usuario == enc.id_usuario)
        nombre_user = user.nombre if user else "Desconocido"
        
        print(f"ID: {enc.id_usuario} | Nombre: {nombre_user} | Nacimiento: {enc.fecha_nacimiento} | País: {enc.pais}")
    print("------------------------------\n")

def ingresar_encuestado():
    print("\n--- INGRESAR ENCUESTADO (Nuevo Usuario) ---")
    rut = input("RUT: ").strip()
    nombre = input("Nombre: ").strip()
    email = input("Email: ").strip()
    contrasena = input("Contraseña: ").strip()
    
    fecha_str = input("Fecha de Nacimiento (YYYY-MM-DD): ").strip()
    genero = input("Género (Opcional): ").strip()
    ocupacion = input("Ocupación (Opcional): ").strip()
    pais = input("País: ").strip()
    
    try:
        fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d").date()
    except ValueError:
        print("Error: Formato de fecha incorrecto. Usa YYYY-MM-DD.")
        return

    if crear_encuestado_completo(rut, nombre, email, contrasena, fecha_obj, genero, ocupacion, pais):
        print("¡Encuestado y Usuario guardados con éxito!")
    else:
        print("❌ No se pudo guardar.")

def modificar_encuestado():
    print("\n--- MODIFICAR ENCUESTADO ---")
    id_usuario = input("ID del encuestado a modificar: ").strip()
    
    encuestado = obtener_encuestado_id(id_usuario)
    if not encuestado:
        print("Error: No existe el encuestado.")
        return

    usuario = Usuario.get_or_none(Usuario.id_usuario == id_usuario)
    
    # NUEVA VALIDACIÓN: Si el usuario no existe, evitamos que el programa explote
    if not usuario:
        print("Error crítico: El encuestado existe, pero su cuenta de usuario fue eliminada.")
        return
    
    # A partir de aquí, VS Code ya sabe que 'usuario' no es None y no marcará error
    nuevo_nombre = input(f"Nuevo Nombre (actual: {usuario.nombre}): ").strip()
    nuevo_email = input(f"Nuevo Email (actual: {usuario.email}): ").strip()
    nueva_contrasena = input("Nueva Contraseña (dejar vacío para no cambiar): ").strip()
    
    
    fecha_str = input(f"Nueva Fecha Nacimiento (actual: {encuestado.fecha_nacimiento}): ").strip()
    fecha_obj = None
    if fecha_str:
        try:
            fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        except ValueError:
            print("Error: Formato de fecha incorrecto. No se actualizará la fecha.")

    nuevo_genero = input(f"Nuevo Género (actual: {encuestado.genero}): ").strip()
    nueva_ocupacion = input(f"Nueva Ocupación (actual: {encuestado.ocupacion}): ").strip()
    nuevo_pais = input(f"Nuevo País (actual: {encuestado.pais}): ").strip()

    if modificar_encuestado_completo(encuestado, nuevo_nombre, nuevo_email, nueva_contrasena, fecha_obj, nuevo_genero, nueva_ocupacion, nuevo_pais):
        print("¡Encuestado y Usuario modificados con éxito!")
    else:
        print("❌ No se pudo modificar.")

def eliminar_encuestado():
    print("\n--- ELIMINAR ENCUESTADO ---")
    id_usuario = input("ID del encuestado a eliminar: ").strip()
    
    encuestado = obtener_encuestado_id(id_usuario)
    if not encuestado:
        print("Error: No existe el encuestado.")
        return

    if eliminar_encuestado_bd(encuestado):
        print("¡Encuestado y su Usuario eliminados con éxito!")
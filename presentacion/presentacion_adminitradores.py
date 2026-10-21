from datetime import datetime
from datos.modelos.Administrador import Administrador
from datos.repositorio.repo_administrador import (
    listado_administradores, 
    obtener_administrador_id, 
    eliminar_administrador_bd
)
# IMPORTANTE: Importamos la nueva función del negocio
from negocio.negocio_administrador import crear_administrador_completo 

def mostrar_listado_administradores():
    administradores = listado_administradores()
    print("\n--- LISTADO DE ADMINISTRADORES ---")
    for admin in administradores:
        print(f"ID Usuario: {admin.id_usuario} | Cargo: {admin.cargo} | Fecha: {admin.fecha_contratacion}")
    print("----------------------------------\n")

def ingresar_administrador():
    print("\n--- INGRESAR ADMINISTRADOR (Nuevo Usuario) ---")
    
    # 1. Pedimos los datos del Usuario (Padre)
    rut = input("RUT: ").strip()
    nombre = input("Nombre: ").strip()
    email = input("Email: ").strip()
    contrasena = input("Contraseña: ").strip()
    
    # 2. Pedimos los datos del Administrador (Hijo)
    cargo = input("Cargo: ").strip()
    fecha_str = input("Fecha de Contratación (YYYY-MM-DD): ").strip()
    
    # 3. Convertimos la fecha
    try:
        fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d").date()
    except ValueError:
        print("Error: Formato de fecha incorrecto. Usa YYYY-MM-DD.")
        return

    # 4. Llamamos al negocio para que guarde en ambas tablas
    if crear_administrador_completo(rut, nombre, email, contrasena, cargo, fecha_obj):
        print("¡Administrador y Usuario guardados con éxito!")
    else:
        print("❌ No se pudo guardar.")

# (El resto de tus funciones modificar_administrador y eliminar_administrador se quedan igual)
def modificar_administrador():
    print("\n--- MODIFICAR ADMINISTRADOR ---")
    id_usuario = input("ID del administrador a modificar: ").strip()
    admin = obtener_administrador_id(id_usuario)
    
    if not admin:
        print("Error: No existe el administrador.")
        return

    cargo = input(f"Nuevo Cargo (actual: {admin.cargo}): ").strip()
    fecha_str = input(f"Nueva Fecha (actual: {admin.fecha_contratacion}): ").strip()

    if cargo:
        admin.cargo = cargo
        
    if fecha_str:
        try:
            admin.fecha_contratacion = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        except ValueError:
            print("Error: Formato de fecha incorrecto. No se actualizará la fecha.")

    try:
        admin.save()
        print("¡Administrador modificado con éxito!")
    except Exception as e:
        print(f"🚨 Error al modificar: {e}")

def eliminar_administrador():
    print("\n--- ELIMINAR ADMINISTRADOR ---")
    id_usuario = input("ID del administrador a eliminar: ").strip()
    admin = obtener_administrador_id(id_usuario)
    
    if not admin:
        print("Error: No existe el administrador.")
        return

    if eliminar_administrador_bd(admin):
        print("¡Administrador eliminado con éxito!")
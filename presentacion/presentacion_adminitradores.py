import bcrypt
from getpass import getpass
from datetime import datetime, date
from negocio.negocio_administrador import (
    crear_administrador_completo,
    procesar_listado_administradores,
    obtener_administrador_por_id,
    modificar_objeto_administrador,
    desactivar_administrador,
)
from auxiliares.validaciones import validar_contrasena, validar_correo, validar_rut

def mostrar_listado_administradores():
    administradores = procesar_listado_administradores()
    print("\n--- LISTADO DE ADMINISTRADORES ---")
    for admin in administradores:
        print(f"ID Usuario: {admin.id_usuario} | Cargo: {admin.cargo} | Fecha: {admin.fecha_contratacion}")
    print("----------------------------------\n")

def ingresar_administrador():
    print("\n--- INGRESAR ADMINISTRADOR (Nuevo Usuario) ---")
    
    rut = ''
    while rut == '':
        rut = input("RUT (ej: 11.111.111-1): ").strip()
        rut = validar_rut(rut)

    nombre = input("Nombre: ").strip()
    
    email = ''
    while email == '':
        email = input("Email: ").strip()
        email = validar_correo(email)
        
    contrasena = ''
    while contrasena == '':
        print("\nRequisitos Contraseña: 8-15 caracteres, 1 mayúscula, 1 minúscula, 1 número, 1 símbolo (!@#$%&/)")
        
        contrasena = getpass("Contraseña: ")
        
        resultado = validar_contrasena(contrasena)
        
        if len(resultado) > 0:
            print("❌ Contraseña inválida:")
            for error in resultado:
                print("-", error)
            contrasena = ''
        else:
            hash_bytes = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
            contrasena = hash_bytes.decode('utf-8')

    cargo = input("Cargo: ").strip()
    fecha_str = input("Fecha de Contratación (YYYY-MM-DD): ").strip()
    
    try:
        fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        
        if fecha_obj > date.today():
            print("Error: La fecha de contratación no puede ser una fecha futura.")
            return
            
    except ValueError:
        print("Error: Formato de fecha incorrecto. Usa YYYY-MM-DD.")
        return


    if crear_administrador_completo(rut, nombre, email, contrasena, cargo, fecha_obj):
        print("¡Administrador y Usuario guardados con éxito!")
    else:
        print("❌ No se pudo guardar.")

def modificar_administrador():
    print("\n--- MODIFICAR ADMINISTRADOR ---")
    id_usuario = input("ID del administrador a modificar: ").strip()
    admin = obtener_administrador_por_id(id_usuario)
    
    if not admin:
        print("Error: No existe el administrador.")
        return

    cargo = input(f"Nuevo Cargo (actual: {admin.cargo}): ").strip()
    fecha_str = input(f"Nueva Fecha (actual: {admin.fecha_contratacion}): ").strip()
    nueva_fecha = None

    if cargo:
        admin.cargo = cargo
        
    if fecha_str:
        try:
            fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d").date()
            
            if fecha_obj > date.today():
                print("Error: La fecha no puede ser futura. No se actualizará.")
            else:
                nueva_fecha = fecha_obj
                
        except ValueError:
            print("Error: Formato de fecha incorrecto. No se actualizará la fecha.")

    if modificar_objeto_administrador(
        admin,
        cargo if cargo else None,
        nueva_fecha,
    ):
        print("¡Administrador modificado con éxito!")

def eliminar_administrador():
    print("\n--- DESACTIVAR ADMINISTRADOR ---")
    id_usuario = input("ID del administrador a desactivar: ").strip()
    admin = obtener_administrador_por_id(id_usuario)
    
    if not admin:
        print("Error: No existe el administrador.")
        return

    if desactivar_administrador(admin):
        print("¡Administrador desactivado con éxito!")
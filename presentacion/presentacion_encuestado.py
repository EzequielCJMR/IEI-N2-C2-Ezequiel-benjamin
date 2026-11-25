import bcrypt
from getpass import getpass
from datetime import datetime, date
from negocio.negocio_encuestado import (
    crear_encuestado_completo, 
    procesar_listado_encuestados,
    modificar_encuestado_completo,
    obtener_encuestado_por_id,
    desactivar_encuestado,
)
from negocio.negocio_usuarios import obtener_usuario_por_id
from auxiliares.validaciones import validar_contrasena, validar_correo, validar_rut

def mostrar_listado_encuestados():
    encuestados = procesar_listado_encuestados()
    print("\n--- LISTADO DE ENCUESTADOS ---")
    if not encuestados:
        print("No hay encuestados registrados.")
        return
        
    for enc in encuestados:
        user = obtener_usuario_por_id(enc.id_usuario)
        nombre_user = user.nombre if user else "Desconocido"
        print(f"ID: {enc.id_usuario} | Nombre: {nombre_user} | Nacimiento: {enc.fecha_nacimiento} | País: {enc.pais}")
    print("------------------------------\n")

def ingresar_encuestado():
    print("\n--- INGRESAR ENCUESTADO (Nuevo Usuario) ---")
    
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
    
    fecha_str = input("Fecha de Nacimiento (YYYY-MM-DD): ").strip()
    genero = input("Género (Opcional): ").strip()
    ocupacion = input("Ocupación (Opcional): ").strip()
    pais = input("País: ").strip()
    
    try:
        fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        if fecha_obj > date.today():
            print("Error: La fecha de nacimiento no puede ser en el futuro.")
            return
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
    
    encuestado = obtener_encuestado_por_id(id_usuario)
    if not encuestado:
        print("Error: No existe el encuestado.")
        return

    usuario = obtener_usuario_por_id(id_usuario)
    if not usuario:
        print("Error crítico: El encuestado existe, pero su cuenta de usuario fue eliminada.")
        return
    
    nuevo_nombre = input(f"Nuevo Nombre (actual: {usuario.nombre}): ").strip()
    nuevo_email = input(f"Nuevo Email (actual: {usuario.email}): ").strip()
    
    print("Nueva Contraseña (dejar vacío para no cambiar):")
    nueva_contrasena = getpass("Contraseña: ")
    
    if nueva_contrasena:
        resultado = validar_contrasena(nueva_contrasena)
        if len(resultado) > 0:
            print("❌ La contraseña no cumple los requisitos. No se modificará.")
            nueva_contrasena = ''
        else:
            hash_bytes = bcrypt.hashpw(nueva_contrasena.encode('utf-8'), bcrypt.gensalt())
            nueva_contrasena = hash_bytes.decode('utf-8')
    else:
        nueva_contrasena = usuario.contrasena
    
    fecha_str = input(f"Nueva Fecha Nacimiento (actual: {encuestado.fecha_nacimiento}): ").strip()
    fecha_obj = None
    if fecha_str:
        try:
            fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d").date()
            if fecha_obj > date.today():
                print("Error: La fecha de nacimiento no puede ser en el futuro. No se actualizará.")
                fecha_obj = None
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
    print("\n--- DESACTIVAR ENCUESTADO ---")
    id_usuario = input("ID del encuestado a desactivar: ").strip()
    
    encuestado = obtener_encuestado_por_id(id_usuario)
    if not encuestado:
        print("Error: No existe el encuestado.")
        return

    if desactivar_encuestado(encuestado):
        print("¡Encuestado desactivado con éxito!")
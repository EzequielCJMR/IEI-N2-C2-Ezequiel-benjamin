import bcrypt
from datos.modelos.usuario import Usuario
from negocio.negocio_usuarios import (
    procesar_listado_usuarios, 
    crear_objeto_usuario, 
    modificar_objeto_usuario
)
from datos.repositorio.repo_usuarios import obtener_usuario_id, eliminar_usuario_bd
from auxiliares.validaciones import validar_contrasena, validar_correo

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
    
    email = ''
    while email == '':
        email = input("Email: ").strip()
        email = validar_correo(email)

    rol = input("Rol (Administrador/Encuestado): ").strip()

    contrasena = ''
    while contrasena == '':
        print("\nRequisitos Contraseña:")
        print("- Entre 8 y 15 caracteres\n- Al menos una mayúscula\n- Al menos una minúscula\n- Al menos un número\n- Al menos un símbolo: !@#$%&/")
        contrasena = input("Contraseña: ").strip()
        
        resultado = validar_contrasena(contrasena)
        
        if len(resultado) > 0:
            print("❌ Contraseña inválida. Errores:")
            for error in resultado:
                print("-", error)
            contrasena = ''
        else:
            hash_bytes = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
            contrasena_encriptada = hash_bytes.decode('utf-8')

    if crear_objeto_usuario(nombre, rut, email, contrasena_encriptada, rol):
        print("¡Usuario guardado con éxito! (Contraseña segura)")

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
    
    contrasena_nueva = input(f"Nueva Contraseña (dejar vacío para no cambiar): ").strip()
    if contrasena_nueva:
        resultado = validar_contrasena(contrasena_nueva)
        if len(resultado) > 0:
            print("❌ La contraseña no cumple los requisitos. No se modificará.")
            contrasena_nueva = ''
        else:
            hash_bytes = bcrypt.hashpw(contrasena_nueva.encode('utf-8'), bcrypt.gensalt())
            contrasena_nueva = hash_bytes.decode('utf-8')
    else:
        contrasena_nueva = user.contrasena 

    rol = input(f"Nuevo Rol (actual: {user.rol}): ").strip()

    if modificar_objeto_usuario(user, nombre, email, contrasena_nueva, rol):
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
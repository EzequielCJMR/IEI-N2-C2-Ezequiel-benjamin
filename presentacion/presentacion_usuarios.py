import bcrypt
from getpass import getpass
from negocio.negocio_usuarios import (
    procesar_listado_usuarios, 
    crear_objeto_usuario, 
    modificar_objeto_usuario,
    obtener_usuario_por_id,
    desactivar_usuario,
    verificar_login_usuario,
)
from auxiliares.validaciones import validar_contrasena, validar_correo, validar_rut

from auxiliares import (
    nombre_app, version_app,)

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
    
    rut = ''
    while rut == '':
        rut = input("RUT (ej: 11.111.111-1): ").strip()
        rut = validar_rut(rut)
    
    email = ''
    while email == '':
        email = input("Email: ").strip()
        email = validar_correo(email)

    # VALIDACIÓN DEL ROL
    rol = ''
    while rol not in ['Administrador', 'Encuestado']:
        rol = input("Rol (Administrador/Encuestado): ").strip().capitalize()
        if rol not in ['Administrador', 'Encuestado']:
            print("❌ Error: El rol debe ser exactamente 'Administrador' o 'Encuestado'.")

    contrasena = ''
    while contrasena == '':
        print("\nRequisitos Contraseña:")
        print("- Entre 8 y 15 caracteres\n- Al menos una mayúscula\n- Al menos una minúscula\n- Al menos un número\n- Al menos un símbolo: !@#$%&/")
        
        # ¡AQUÍ USAMOS MASKPASS!
        # CAMBIO: getpass reemplaza maskpass para evitar UnicodeDecodeError.
        contrasena = getpass("Contraseña: ")
        
        # CAMBIO: se valida el texto obtenido antes de generar el hash.
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

    user = obtener_usuario_por_id(id_usuario)
    if not user:
        print("Error: No existe un usuario con ese ID.")
        return

    nombre = input(f"Nuevo Nombre (actual: {user.nombre}): ").strip()
    email = input(f"Nuevo Email (actual: {user.email}): ").strip()
    
    print(f"Nueva Contraseña (dejar vacío para no cambiar):")
    # ¡AQUÍ TAMBIÉN USAMOS MASKPASS!
    # CAMBIO: getpass reemplaza maskpass al modificar la contraseña.
    contrasena_nueva = getpass("Contraseña: ")
    
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

    # VALIDACIÓN DEL ROL AL MODIFICAR
    rol = input(f"Nuevo Rol (actual: {user.rol}) [Dejar vacío para conservar]: ").strip().capitalize()
    if not rol:
        rol = user.rol
    elif rol not in ['Administrador', 'Encuestado']:
        print("❌ Rol inválido. Se mantendrá el rol actual.")
        rol = user.rol

    if modificar_objeto_usuario(user, nombre, email, contrasena_nueva, rol):
        print("¡Usuario modificado con éxito!")

def eliminar_usuario():
    print("\n--- DESACTIVAR USUARIO ---")
    try:
        id_usuario = int(input("ID del usuario a desactivar: ").strip())
    except ValueError:
        print("Error: El ID debe ser un número.")
        return

    user = obtener_usuario_por_id(id_usuario)
    if not user:
        print("Error: No existe un usuario con ese ID.")
        return

    if desactivar_usuario(user):
        print("¡Usuario desactivado con éxito!")


def solicitar_correo(prompt="Correo: "):
    while True:
        correo = input(prompt).strip()
        correo = validar_correo(correo)
        if correo:
            return correo


def solicitar_contrasenia(prompt="Contrasena: "):
    # CAMBIO: se usa getpass una sola vez para evitar pedir la contraseña dos
    # veces y eliminar el UnicodeDecodeError que produce maskpass en Windows.
    return getpass(prompt)


def login():
    print("\n--- LOGIN DE USUARIO ---")
    print(f" Bienvenido a {nombre_app} - version {version_app}")
    email = input("Email: ").strip()
    # CAMBIO: getpass mantiene la contraseña oculta y admite caracteres Unicode.
    # CAMBIO: maskpass se intenta primero por compatibilidad con la evaluacion;
    # getpass es el respaldo seguro cuando maskpass falla en Windows/Python 3.14.
    try:
        import maskpass
        password = maskpass.askpass(prompt="Contraseña: ", mask="*")
    except (ImportError, UnicodeDecodeError, OSError, EOFError):
        password = getpass("Contraseña: ")

    usuario = verificar_login_usuario(email, password)

    if usuario:
        if usuario.activo:
            print(f"¡Bienvenido {usuario.nombre}! Rol: {usuario.rol}")
            return True
        else:
            print("Error: Este usuario está desactivado.")
    else:
        print("Error: Email o contraseña incorrectos.")
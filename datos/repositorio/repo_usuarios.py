import bcrypt
from datos.modelos.usuario import Usuario

def listado_usuarios():
    # Solo mostramos los usuarios que están activos
    return Usuario.select().where(Usuario.activo == True)

def listado_usuarios_inactivos():
    # Función extra por si quieres ver los desactivados (como el profe)
    return Usuario.select().where(Usuario.activo == False)

def obtener_usuario_id(id_usuario):
    return Usuario.get_or_none(Usuario.id_usuario == id_usuario)

def buscar_usuario_email(email):
    return Usuario.get_or_none(Usuario.email == email)

def buscar_usuario_rut(rut):
    return Usuario.get_or_none(Usuario.rut == rut)

def verificar_usuario(email, contrasena):
    usuario = buscar_usuario_email(email)
    if not usuario or not usuario.activo:
        return None

    try:
        if bcrypt.checkpw(contrasena.encode("utf-8"), usuario.contrasena.encode("utf-8")):
            return usuario
    except (ValueError, AttributeError):
        return None

    return None

def guardar_usuario(nombre, rut, email, contrasena, rol):
    try:
        Usuario.create(
            nombre=nombre, 
            rut=rut, 
            email=email, 
            contrasena=contrasena, 
            rol=rol
        )
        return True
    except Exception as e:
        print(f"\n🚨 ERROR DE MYSQL: {e}\n")
        return False

def modificar_usuario_bd(user: Usuario, nombre=None, email=None, contrasena=None, rol=None):
    try:
        if nombre:
            user.nombre = nombre
        if email:
            user.email = email
        if contrasena:
            user.contrasena = contrasena
        if rol:
            user.rol = rol
        user.save()
        return True
    except Exception as error:
        print(f"Error al modificar usuario: {error}")
        return False

def eliminar_usuario_bd(user: Usuario):
    try:
        # En lugar de borrar al usuario y sus dependencias, solo lo desactivamos
        user.activo = False
        user.save()
        return True
    except Exception as e:
        print(f"Error al desactivar usuario: {e}")
        return False
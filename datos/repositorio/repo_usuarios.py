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

def eliminar_usuario_bd(user: Usuario):
    try:
        # En lugar de borrar al usuario y sus dependencias, solo lo desactivamos
        user.activo = False
        user.save()
        return True
    except Exception as e:
        print(f"Error al desactivar usuario: {e}")
        return False
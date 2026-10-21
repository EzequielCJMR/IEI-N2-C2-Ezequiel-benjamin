from datos.modelos.Administrador import Administrador
from datos.modelos.usuario import Usuario

def listado_administradores():
    return Administrador.select()

def obtener_administrador_id(id_usuario):
    return Administrador.get_or_none(Administrador.id_usuario == id_usuario)

def guardar_administrador(id_usuario, cargo, fecha_obj):
    try:
        Administrador.create(id_usuario=id_usuario, cargo=cargo, fecha_contratacion=fecha_obj)
        return True
    except Exception as e:
        print(f"\n🚨 ERROR DE MYSQL: {e}\n")
        return False

# ... (tus otras funciones)

def eliminar_administrador_bd(admin: Administrador):
    try:
        # 1. Guardamos el ID del usuario antes de borrar al administrador
        id_usuario = admin.id_usuario
        
        # 2. Borramos al administrador
        admin.delete_instance()
        
        # 3. Buscamos al usuario y lo borramos también
        usuario_a_borrar = Usuario.get_or_none(Usuario.id_usuario == id_usuario)
        if usuario_a_borrar:
            usuario_a_borrar.delete_instance()
            
        return True
    except Exception as e:
        print(f"Error al eliminar: {e}")
        return False
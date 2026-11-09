from datos.modelos.Administrador import Administrador
from datos.modelos.usuario import Usuario

def listado_administradores():
    # Le decimos a Peewee explícitamente cómo unir las tablas
    return (Administrador
            .select()
            .join(Usuario, on=(Administrador.id_usuario == Usuario.id_usuario))
            .where(Usuario.activo == True))

def obtener_administrador_id(id_usuario):
    return Administrador.get_or_none(Administrador.id_usuario == id_usuario)

def guardar_administrador(id_usuario, cargo, fecha_obj):
    try:
        Administrador.create(id_usuario=id_usuario, cargo=cargo, fecha_contratacion=fecha_obj)
        return True
    except Exception as e:
        print(f"\n🚨 ERROR DE MYSQL: {e}\n")
        return False

def eliminar_administrador_bd(admin: Administrador):
    try:
        # Buscamos al usuario asociado a este administrador
        usuario = Usuario.get_or_none(Usuario.id_usuario == admin.id_usuario)
        
        # Si existe, lo desactivamos en lugar de borrarlo
        if usuario:
            usuario.activo = False
            usuario.save()
            
        return True
    except Exception as e:
        print(f"Error al desactivar administrador: {e}")
        return False
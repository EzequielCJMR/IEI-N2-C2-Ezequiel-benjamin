from datos.modelos.Administrador import Administrador
from datos.modelos.usuario import Usuario

def listado_administradores():
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

def modificar_administrador_bd(admin: Administrador, cargo=None, fecha_contratacion=None):
    try:
        if cargo:
            admin.cargo = cargo
        if fecha_contratacion:
            admin.fecha_contratacion = fecha_contratacion
        admin.save()
        return True
    except Exception as error:
        print(f"Error al modificar administrador: {error}")
        return False

def eliminar_administrador_bd(admin: Administrador):
    try:
        usuario = Usuario.get_or_none(Usuario.id_usuario == admin.id_usuario)
        
        if usuario:
            usuario.activo = False
            usuario.save()
            
        return True
    except Exception as e:
        print(f"Error al desactivar administrador: {e}")
        return False
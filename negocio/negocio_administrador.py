from datos.modelos.Administrador import Administrador
from datos.modelos.usuario import Usuario  # <-- NUEVA IMPORTACIÓN
from datos.repositorio.repo_administrador import guardar_administrador, listado_administradores

def procesar_listado_administradores():
    return listado_administradores()

def crear_administrador_completo(rut, nombre, email, contrasena, cargo, fecha_obj):
    try:
        # 1. Creamos el Usuario
        nuevo_usuario = Usuario.create(
            rut=rut, nombre=nombre, email=email, 
            contrasena=contrasena, rol='Administrador'
        )
        
        # 2. Creamos el Administrador SIN el id_administrador (MySQL lo genera solo)
        Administrador.create(
            id_usuario=nuevo_usuario.id_usuario,
            cargo=cargo,
            fecha_contratacion=fecha_obj
        )
        return True
    except Exception as e:
        print(f"🚨 Error al crear: {e}")
        return False

def crear_objeto_administrador(id_usuario, cargo, fecha_obj):
    try:
        return guardar_administrador(id_usuario, cargo, fecha_obj)
    except Exception as e:
        print(f"Error al crear objeto: {e}")
        return False

def modificar_objeto_administrador(admin: Administrador, nuevo_cargo, nueva_fecha_obj):
    try:
        if nuevo_cargo:
            admin.cargo = nuevo_cargo
        if nueva_fecha_obj:
            admin.fecha_contratacion = nueva_fecha_obj
        admin.save()
        return True
    except Exception as e:
        print(f"Error al modificar objeto: {e}")
        return False
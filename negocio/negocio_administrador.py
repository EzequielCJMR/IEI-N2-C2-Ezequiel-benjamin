from datos.modelos.Administrador import Administrador
from datos.modelos.usuario import Usuario
from datos.repositorio.repo_administrador import (
    guardar_administrador,
    listado_administradores,
    obtener_administrador_id,
    modificar_administrador_bd,
    eliminar_administrador_bd,
)
from datos.modelos.base import database

def procesar_listado_administradores():
    return listado_administradores()

def crear_administrador_completo(rut, nombre, email, contrasena, cargo, fecha_obj):
    try:
        if Usuario.get_or_none(Usuario.email == email):
            print("Error: El email ya está registrado.")
            return False
        if Usuario.get_or_none(Usuario.rut == rut):
            print("Error: El RUT ya está registrado.")
            return False

        with database.atomic():
            nuevo_usuario = Usuario.create(
                rut=rut, nombre=nombre, email=email,
                contrasena=contrasena, rol='Administrador'
            )
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
        return modificar_administrador_bd(admin, nuevo_cargo, nueva_fecha_obj)
    except Exception as e:
        print(f"Error al modificar objeto: {e}")
        return False

def obtener_administrador_por_id(id_usuario):
    return obtener_administrador_id(id_usuario)

def desactivar_administrador(admin: Administrador):
    return eliminar_administrador_bd(admin)


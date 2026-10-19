from datetime import datetime  # <-- 1. AGREGAMOS ESTA IMPORTACIÓN ARRIBA
from datos.modelos.Administrador import Administrador

def listado_administradores():
    administradores = Administrador.select()

    for admin in administradores:
        print(admin)
        print(f"ID: {admin.id_usuario}, Cargo: {admin.cargo}, Fecha de Contratación: {admin.fecha_contratacion}")       

#procesar_listado_administradores(tabla:prettytable):
#if tabla:
#    tabla.field_names = ["ID", "Cargo", "Fecha de Contratación"]
#   listado = listado_administradores()
#    if listado:
#        for admin in listado:
#            tabla.add_row([admin.id_usuario, admin.cargo, admin.fecha_contratacion])

def ingresar_administrador():
    id_usuario = input("ID: ").strip()
    cargo = input("Cargo: ").strip()
    fecha = input("Fecha (YYYY-MM-DD): ").strip()

    if Administrador.get_or_none(Administrador.id_usuario == id_usuario):
        print("Ya existe.")
        return

    # 2. CONVERTIMOS EL TEXTO A FECHA ANTES DE CREAR
    fecha_obj = datetime.strptime(fecha, "%Y-%m-%d").date()
    
    Administrador.create(id_usuario=id_usuario, cargo=cargo, fecha_contratacion=fecha_obj)
    print("Guardado.")
    

def modificar_administrador():
    id_usuario = input("ID del administrador a modificar: ").strip()
    admin = Administrador.get_or_none(Administrador.id_usuario == id_usuario)

    if not admin:
        print("No existe.")
        return

    cargo = input(f"Nuevo Cargo (actual: {admin.cargo}): ").strip()
    fecha = input(f"Nueva Fecha de Contratación (actual: {admin.fecha_contratacion}): ").strip()

    if cargo:
        admin.cargo = cargo
        
    if fecha:
        # 3. CONVERTIMOS EL TEXTO A FECHA ANTES DE MODIFICAR
        fecha_obj = datetime.strptime(fecha, "%Y-%m-%d").date()
        admin.fecha_contratacion = fecha_obj

    admin.save()
    print("Modificado.")


def eliminar_administrador():
    id_usuario = input("ID del administrador a eliminar: ").strip()
    admin = Administrador.get_or_none(Administrador.id_usuario == id_usuario)

    if not admin:
        print("No existe.")
        return

    admin.delete_instance()
    print("Eliminado.")
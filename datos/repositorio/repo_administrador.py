from datos.modelos.Administrador import Administrador


def listado_administradores():
    administradores = Administrador.select()

    for admin in administradores:
        print(admin)
        print(f"ID: {admin.id_usuario}, Cargo: {admin.cargo}, Fecha de Contratación: {admin.fecha_contratacion}")       


def ingresar_administrador():
    id_usuario = input("ID: ").strip()
    cargo = input("Cargo: ").strip()
    fecha = input("Fecha (YYYY-MM-DD): ").strip()

    if Administrador.get_or_none(Administrador.id_usuario == id_usuario):
        print("Ya existe.")
        return

    Administrador.create(id_usuario=id_usuario, cargo=cargo, fecha_contratacion=fecha)
    print("Guardado.")
from datos.modelos.usuario import Usuario


def listado_usuarios():
    usuarios = Usuario.select()
    print("listado de usuarios")

    for user in usuarios:
        print(user)
        print(f"ID: {user.id_usuario}, Nombre: {user.nombre}, Email: {user.email}")


def ingresar_usuario():
    nombre = input("Nombre: ").strip()
    rut = input("RUT: ").strip()
    email = input("Email: ").strip()
    contrasena = input("Contraseña: ").strip()
    rol = input("Rol: ").strip()

    if Usuario.get_or_none(Usuario.email == email):
        print("Ya existe ese email.")
        return
    if Usuario.get_or_none(Usuario.rut == rut):
        print("Ya existe ese RUT.")
        return

    Usuario.create(nombre=nombre, rut=rut, email=email, contrasena=contrasena, rol=rol)
    print("Guardado.")

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


def modificar_usuario():
    print("\n--- MODIFICAR USUARIO ---")
    # Como el ID es autoincremental, pedimos el ID para buscar
    try:
        id_usuario = int(input("ID del usuario a modificar: ").strip())
    except ValueError:
        print("Error: El ID debe ser un número.")
        return

    user = Usuario.get_or_none(Usuario.id_usuario == id_usuario)

    if not user:
        print("Error: No existe un usuario con ese ID.")
        return

    # Pedimos los datos nuevos (si se deja vacío, se mantiene el actual)
    nombre = input(f"Nuevo Nombre (actual: {user.nombre}): ").strip()
    email = input(f"Nuevo Email (actual: {user.email}): ").strip()
    contrasena = input(f"Nueva Contraseña (actual: {user.contrasena}): ").strip()
    rol = input(f"Nuevo Rol (actual: {user.rol}): ").strip()

    # Actualizamos solo si el usuario escribió algo
    if nombre:
        user.nombre = nombre
    if email:
        # Validar que el nuevo email no esté ocupado por OTRO usuario
        if Usuario.get_or_none((Usuario.email == email) & (Usuario.id_usuario != id_usuario)):
            print("Error: Ese email ya está en uso por otro usuario.")
            return
        user.email = email
    if contrasena:
        user.contrasena = contrasena
    if rol:
        user.rol = rol

    user.save()
    print("¡Usuario modificado con éxito!")


def eliminar_usuario():
    print("\n--- ELIMINAR USUARIO ---")
    try:
        id_usuario = int(input("ID del usuario a eliminar: ").strip())
    except ValueError:
        print("Error: El ID debe ser un número.")
        return

    user = Usuario.get_or_none(Usuario.id_usuario == id_usuario)

    if not user:
        print("Error: No existe un usuario con ese ID.")
        return

    user.delete_instance()
    print("¡Usuario eliminado con éxito!")
from datos.modelos.usuario import Usuario

from datos.repositorio.repo_usuarios import guardar_usuario, listado_usuarios, buscar_usuario_email, buscar_usuario_rut

def procesar_listado_usuarios():
    return listado_usuarios()

def crear_objeto_usuario(nombre, rut, email, contrasena, rol):
    try:
        # Validaciones
        if buscar_usuario_email(email):
            print("Error: Ya existe un usuario con ese email.")
            return False
        if buscar_usuario_rut(rut):
            print("Error: Ya existe un usuario con ese RUT.")
            return False
            
        return guardar_usuario(nombre, rut, email, contrasena, rol)
    except Exception as e:
        print(f"Error al crear objeto: {e}")
        return False

def modificar_objeto_usuario(user: Usuario, nuevo_nombre, nuevo_email, nueva_contrasena, nuevo_rol):
    try:
        if nuevo_nombre:
            user.nombre = nuevo_nombre
            
        if nuevo_email:
            # 1. Buscamos al usuario con ese email (o None si no existe)
            usuario_con_ese_email = buscar_usuario_email(nuevo_email)
            
            # 2. Validamos: Si existe Y NO es el mismo usuario que estamos modificando
            if usuario_con_ese_email and usuario_con_ese_email.id_usuario != user.id_usuario:
                print("Error: Ese email ya está en uso por otro usuario.")
                return False
                
            user.email = nuevo_email
            
        if nueva_contrasena:
            user.contrasena = nueva_contrasena
        if nuevo_rol:
            user.rol = nuevo_rol
            
        user.save() # Guardamos los cambios
        return True
    except Exception as e:
        print(f"Error al modificar objeto: {e}")
        return False
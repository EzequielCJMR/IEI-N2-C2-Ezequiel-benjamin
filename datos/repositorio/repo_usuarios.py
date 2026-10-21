from datos.modelos.usuario import Usuario
from datos.modelos.Administrador import Administrador
from datos.modelos.encuestado import Encuestado

def listado_usuarios():
    return Usuario.select()

def obtener_usuario_id(id_usuario):
    return Usuario.get_or_none(Usuario.id_usuario == id_usuario)

def buscar_usuario_email(email):
    return Usuario.get_or_none(Usuario.email == email)

def buscar_usuario_rut(rut):
    return Usuario.get_or_none(Usuario.rut == rut)

def guardar_usuario(nombre, rut, email, contrasena, rol):
    try:
        # Usamos .create() igual que en administrador para que guarde al instante
        Usuario.create(
            nombre=nombre, 
            rut=rut, 
            email=email, 
            contrasena=contrasena, 
            rol=rol
        )
        return True
    except Exception as e:
        print(f"\n🚨 ERROR DE MYSQL: {e}\n")
        return False

def eliminar_usuario_bd(user: Usuario):
    try:
        # 1. Guardamos el ID del usuario
        id_usuario = user.id_usuario
        
        # 2. Buscamos y borramos si es Administrador
        admin_asociado = Administrador.get_or_none(Administrador.id_usuario == id_usuario)
        if admin_asociado:
            admin_asociado.delete_instance()
            
        # 3. Buscamos y borramos si es Encuestado
        encuestado_asociado = Encuestado.get_or_none(Encuestado.id_usuario == id_usuario)
        if encuestado_asociado:
            encuestado_asociado.delete_instance()

        # 4. Finalmente, borramos al Usuario
        user.delete_instance()
        
        return True
    except Exception as e:
        print(f"Error al eliminar usuario: {e}")
        return False
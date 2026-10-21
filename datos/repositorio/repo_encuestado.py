from datos.modelos.encuestado import Encuestado
from datos.modelos.usuario import Usuario

def listado_encuestados():
    return Encuestado.select()

def obtener_encuestado_id(id_usuario):
    return Encuestado.get_or_none(Encuestado.id_usuario == id_usuario)

def eliminar_encuestado_bd(encuestado: Encuestado):
    try:
        # 1. Guardamos el ID
        id_usuario = encuestado.id_usuario
        
        # 2. Borramos al encuestado
        encuestado.delete_instance()
        
        # 3. Borramos también su usuario asociado
        usuario = Usuario.get_or_none(Usuario.id_usuario == id_usuario)
        if usuario:
            usuario.delete_instance()
            
        return True
    except Exception as e:
        print(f"Error al eliminar: {e}")
        return False
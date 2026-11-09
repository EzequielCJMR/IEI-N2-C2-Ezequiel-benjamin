from datos.modelos.encuestado import Encuestado
from datos.modelos.usuario import Usuario

def listado_encuestados():
    return (Encuestado
            .select()
            .join(Usuario, on=(Encuestado.id_usuario == Usuario.id_usuario))
            .where(Usuario.activo == True))

def obtener_encuestado_id(id_usuario):
    return Encuestado.get_or_none(Encuestado.id_usuario == id_usuario)

def eliminar_encuestado_bd(encuestado: Encuestado):
    try:
        # Buscamos al usuario asociado a este encuestado
        usuario = Usuario.get_or_none(Usuario.id_usuario == encuestado.id_usuario)
        
        # Si existe, lo desactivamos en lugar de borrarlo
        if usuario:
            usuario.activo = False
            usuario.save()
            
        return True
    except Exception as e:
        print(f"Error al desactivar encuestado: {e}")
        return False
from datos.modelos.encuestado import Encuestado
from datos.modelos.usuario import Usuario

def listado_encuestados():
    return (Encuestado
            .select()
            .join(Usuario, on=(Encuestado.id_usuario == Usuario.id_usuario))
            .where(Usuario.activo == True))

def obtener_encuestado_id(id_usuario):
    return Encuestado.get_or_none(Encuestado.id_usuario == id_usuario)

def modificar_encuestado_bd(encuestado: Encuestado, fecha_nacimiento=None, genero=None, ocupacion=None, pais=None):
    try:
        if fecha_nacimiento:
            encuestado.fecha_nacimiento = fecha_nacimiento
        if genero:
            encuestado.genero = genero
        if ocupacion:
            encuestado.ocupacion = ocupacion
        if pais:
            encuestado.pais = pais
        encuestado.save()
        return True
    except Exception as error:
        print(f"Error al modificar encuestado: {error}")
        return False

def eliminar_encuestado_bd(encuestado: Encuestado):
    try:
        usuario = Usuario.get_or_none(Usuario.id_usuario == encuestado.id_usuario)
        
        if usuario:
            usuario.activo = False
            usuario.save()
            
        return True
    except Exception as e:
        print(f"Error al desactivar encuestado: {e}")
        return False
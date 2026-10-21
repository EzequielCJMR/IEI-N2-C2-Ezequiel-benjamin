from datos.modelos.encuestado import Encuestado
from datos.modelos.usuario import Usuario
from datos.repositorio.repo_encuestado import listado_encuestados

def procesar_listado_encuestados():
    return listado_encuestados()

def crear_encuestado_completo(rut, nombre, email, contrasena, fecha_nac_obj, genero, ocupacion, pais):
    try:
        if Usuario.get_or_none(Usuario.email == email):
            print("Error: El email ya está registrado.")
            return False
        if Usuario.get_or_none(Usuario.rut == rut):
            print("Error: El RUT ya está registrado.")
            return False

        # 1. Creamos el Usuario
        nuevo_usuario = Usuario.create(
            rut=rut, nombre=nombre, email=email, 
            contrasena=contrasena, rol='Encuestado'
        )
        
        # 2. Creamos al Encuestado
        Encuestado.create(
            id_usuario=nuevo_usuario.id_usuario,
            fecha_nacimiento=fecha_nac_obj,
            genero=genero,
            ocupacion=ocupacion,
            pais=pais
        )
        return True
    except Exception as e:
        print(f"🚨 Error al crear: {e}")
        return False

# NUEVA FUNCIÓN PARA MODIFICAR
def modificar_encuestado_completo(encuestado, nuevo_nombre, nuevo_email, nueva_contrasena, nueva_fecha_obj, nuevo_genero, nueva_ocupacion, nuevo_pais):
    try:
        # 1. Actualizamos los datos del Usuario
        usuario = Usuario.get_or_none(Usuario.id_usuario == encuestado.id_usuario)
        if usuario:
            if nuevo_nombre:
                usuario.nombre = nuevo_nombre
            if nuevo_email:
                usuario.email = nuevo_email
            if nueva_contrasena:
                usuario.contrasena = nueva_contrasena
            usuario.save()
            
        # 2. Actualizamos los datos del Encuestado
        if nueva_fecha_obj:
            encuestado.fecha_nacimiento = nueva_fecha_obj
        if nuevo_genero:
            encuestado.genero = nuevo_genero
        if nueva_ocupacion:
            encuestado.ocupacion = nueva_ocupacion
        if nuevo_pais:
            encuestado.pais = nuevo_pais
            
        encuestado.save()
        return True
    except Exception as e:
        print(f"🚨 Error al modificar: {e}")
        return False
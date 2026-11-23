from auxiliares import (
    nombre_app, version_app, 
    titulo_principal, diccionario_menu_principal,
    menu_administrador, diccionario_menu_administrador,
    menu_usuario, diccionario_menu_usuario,
    menu_encuestado, diccionario_menu_encuestado,
    menu_categoria, diccionario_menu_categoria,
    menu_encuesta, diccionario_menu_encuesta,
    menu_encuestado_sesion, diccionario_menu_encuestado_sesion
)

# Importamos tus CRUDs
from presentacion.presentacion_adminitradores import (
    mostrar_listado_administradores, ingresar_administrador, 
    modificar_administrador, eliminar_administrador
)
from presentacion.presentacion_usuarios import (
    mostrar_listado_usuarios, ingresar_usuario, 
    modificar_usuario, eliminar_usuario
)
from presentacion.presentacion_encuestado import (
    mostrar_listado_encuestados, ingresar_encuestado, 
    modificar_encuestado, eliminar_encuestado
)
from presentacion.presentacion_categoria import (
    mostrar_listado_categorias, ingresar_categoria,
    modificar_categoria_presentacion, eliminar_categoria_presentacion
)
from presentacion.presentacion_encuesta import (
    mostrar_listado_encuestas, ingresar_encuesta,
    modificar_encuesta_presentacion, eliminar_encuesta_presentacion
)

# CAMBIO: el menu usa funciones de negocio para mostrar datos segun el rol.
from negocio.negocio_encuestado import obtener_encuestado_por_id
from negocio.negocio_encuesta import procesar_listado_encuestas_publicadas

from auxiliares import (
    nombre_app, version_app
)



def mostrar_menu(titulo, opciones):
    print("\n" + "=" * 40)
    print(f"Bienvenido a {nombre_app} - version {version_app}")
    print("=" * 40)
    print(titulo)
    print(f'{"=" * len(titulo)}\n')
    for clave, valor in opciones.items():
        print(f'[{clave}] - {valor}')

# --- SUBMENÚS --

def cargar_menu_administrador():
    while True:
        mostrar_menu(menu_administrador, diccionario_menu_administrador)
        opcion = input('Seleccione su opción: ').strip()
        print()
        match opcion:
            case '1': mostrar_listado_administradores()
            case '2': ingresar_administrador()
            case '3': modificar_administrador()
            case '4': eliminar_administrador()
            case '0': break
            case _: print('Opción no válida.')

def cargar_menu_usuario():
    while True:
        mostrar_menu(menu_usuario, diccionario_menu_usuario)
        opcion = input('Seleccione su opción: ').strip()
        print()
        match opcion:
            case '1': mostrar_listado_usuarios()
            case '2': ingresar_usuario()
            case '3': modificar_usuario()
            case '4': eliminar_usuario()
            case '0': break
            case _: print('Opción no válida.')

def cargar_menu_encuestado():
    while True:
        mostrar_menu(menu_encuestado, diccionario_menu_encuestado)
        opcion = input('Seleccione su opción: ').strip()
        print()
        match opcion:
            case '1': mostrar_listado_encuestados()
            case '2': ingresar_encuestado()
            case '3': modificar_encuestado()
            case '4': eliminar_encuestado()
            case '0': break
            case _: print('Opción no válida.')

def cargar_menu_categoria():
    while True:
        mostrar_menu(menu_categoria, diccionario_menu_categoria)
        opcion = input('Seleccione su opción: ').strip()
        print()
        match opcion:
            case '1': mostrar_listado_categorias()
            case '2': ingresar_categoria()
            case '3': modificar_categoria_presentacion()
            case '4': eliminar_categoria_presentacion()
            case '0': break
            case _: print('Opción no válida.')

def cargar_menu_encuesta():
    while True:
        mostrar_menu(menu_encuesta, diccionario_menu_encuesta)
        opcion = input('Seleccione su opción: ').strip()
        print()
        match opcion:
            case '1': mostrar_listado_encuestas()
            case '2': ingresar_encuesta()
            case '3': modificar_encuesta_presentacion()
            case '4': eliminar_encuesta_presentacion()
            case '0': break
            case _: print('Opción no válida.')

# --- MENÚ PRINCIPAL ---

def cargar_menu_encuestado_sesion(usuario):
    while True:
        mostrar_menu(
            menu_encuestado_sesion,
            diccionario_menu_encuestado_sesion
        )
        opcion = input('Seleccione su opción: ').strip()
        print()
        match opcion:
            case '1':
                encuestado = obtener_encuestado_por_id(usuario.id_usuario)
                if encuestado:
                    print('\n--- MI PERFIL ---')
                    print(f'Nombre: {usuario.nombre}')
                    print(f'Email: {usuario.email}')
                    print(f'RUT: {usuario.rut}')
                    print(f'Fecha de nacimiento: {encuestado.fecha_nacimiento}')
                    print(f'Género: {encuestado.genero or "-"}')
                    print(f'Ocupación: {encuestado.ocupacion or "-"}')
                    print(f'País: {encuestado.pais}')
                else:
                    print('No existe el perfil de encuestado asociado.')
            case '2':
                encuestas = procesar_listado_encuestas_publicadas()
                print('\n--- ENCUESTAS PUBLICADAS ---')
                if not encuestas:
                    print('No hay encuestas publicadas.')
                else:
                    for encuesta in encuestas:
                        print(
                            f"ID: {encuesta.id_encuesta} | "
                            f"Título: {encuesta.titulo} | "
                            f"Expira: {encuesta.fecha_expiracion or '-'}"
                        )
            case '0':
                print('Cerrando sesión...')
                break
            case _: print('Opción no válida.')


# CAMBIO: el menú recibe el usuario autenticado y aplica permisos por rol.
def cargar_menu(usuario=None):
    if not usuario:
        print('Debe iniciar sesión.')
        return

    rol = usuario.rol.strip().lower()
    if rol == 'encuestado':
        cargar_menu_encuestado_sesion(usuario)
        return
    if rol != 'administrador':
        print('Rol no autorizado.')
        return

    while True:
        mostrar_menu(titulo_principal, diccionario_menu_principal)
   
        opcion = input('Seleccione su opción: ').strip()
        print()

        match opcion:
            case '1':
                cargar_menu_administrador()
            case '2':
                cargar_menu_usuario()
            case '3':
                cargar_menu_encuestado()
            case '4':
                cargar_menu_categoria()
            case '5':
                cargar_menu_encuesta()
            case '0':
                print('Saliendo del programa...')
                break
            case _:
                print('Opción no válida. Intente de nuevo.')
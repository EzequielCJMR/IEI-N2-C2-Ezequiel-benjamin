from auxiliares import (
    nombre_app, version_app, 
    titulo_principal, diccionario_menu_principal,
    menu_administrador, diccionario_menu_administrador,
    menu_usuario, diccionario_menu_usuario,
    menu_encuestado, diccionario_menu_encuestado
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
from datos.conexion import conectar

def mostrar_menu(titulo, opciones):
    print("\n" + "=" * 40)
    print(f"Bienvenido a {nombre_app} - version {version_app}")
    print("=" * 40)
    print(titulo)
    print(f'{"=" * len(titulo)}\n')
    for clave, valor in opciones.items():
        print(f'[{clave}] - {valor}')

# --- SUBMENÚS ---

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

# --- MENÚ PRINCIPAL ---

def cargar_menu():
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
            case '0':
                print('Saliendo del programa...')
                db = conectar()
                if not db.is_closed():
                    db.close()
                break
            case _:
                print('Opción no válida. Intente de nuevo.')
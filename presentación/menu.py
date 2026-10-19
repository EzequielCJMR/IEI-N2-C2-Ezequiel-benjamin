from auxiliares.datos_app import nombre_app, version_app

from datos.repositorio.repo_administrador import listado_administradores
from datos.repositorio.repo_administrador import ingresar_administrador
from datos.repositorio.repo_administrador import modificar_administrador
from datos.repositorio.repo_administrador import eliminar_administrador
from datos.repositorio.repo_usuarios import listado_usuarios
from datos.repositorio.repo_usuarios import ingresar_usuario
from datos.repositorio.repo_usuarios import modificar_usuario
from datos.repositorio.repo_usuarios import eliminar_usuario


    

def menu_principal():
    print("Bienvenido al sistema de Encuestas")
    print(f"cargando {nombre_app} - version {version_app}")

    print("Menú Principal:")
    print("1. Listar Administradores")
    print("2. Ingresar un Administrador")
    print("3. Modificar un Administrador")
    print("4. Eliminar un Administrador")
    print("5. listar  Usuarios")
    print("6. Ingresar un Usuario")
    print("7. modificar un Usuario")
    print("8. eliminar un Usuario")
    print("10. Salir")

    opcion = input("Seleccione una opción (1-10): ").strip()

    if opcion == "1":
        listado_administradores()
    elif opcion == "2":
        ingresar_administrador()
    elif opcion == "3":
        modificar_administrador()
    elif opcion == "4":
        eliminar_administrador()
    elif opcion == "5":
        listado_usuarios()
    elif opcion == "6":
        ingresar_usuario()
    elif opcion == "7":
        modificar_usuario()
    elif opcion == "8":
        eliminar_usuario()
    elif opcion == "10":
        print("Saliendo del programa...")
        exit()


def cargar_menu():
    print("Bienvenido al sistema de Encuestas")
    print(f"cargando {nombre_app} - version {version_app}")



    listado_administradores()
    listado_usuarios()

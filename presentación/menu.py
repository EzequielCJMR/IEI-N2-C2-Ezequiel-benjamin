from auxiliares.datos_app import nombre_app, version_app

from datos.repositorio.repo_administrador import listado_administradores
from datos.repositorio.repo_administrador import ingresar_administrador
from datos.repositorio.repo_usuarios import listado_usuarios
from datos.repositorio.repo_usuarios import ingresar_usuario



def menu_principal():
    print("Bienvenido al sistema de Encuestas")
    print(f"cargando {nombre_app} - version {version_app}")

    print("Menú Principal:")
    print("1. Listar Administradores")
    print("2. Ingresar un Administrador")
    print("3. Listar Usuarios")
    print("4. Ingresar un Usuario")
    print("10. Salir")

    opcion = input("Seleccione una opción (1-4): ").strip()

    if opcion == "1":
        listado_administradores()
    elif opcion == "2":
        ingresar_administrador()
    elif opcion == "3":
        listado_usuarios()
    elif opcion == "4":
        ingresar_usuario()
    elif opcion == "10":
        print("Saliendo del sistema. ¡Hasta luego!")
        exit()




def cargar_menu():
    print("Bienvenido al sistema de Encuestas")
    print(f"cargando {nombre_app} - version {version_app}")



    listado_administradores()
    listado_usuarios()

import bcrypt

from auxiliares import nombre_app, version_app
from presentacion.presentacion_usuarios import solicitar_correo, solicitar_contrasenia
from presentacion import cargar_menu
from negocio import usuario_por_correo



def login_usuario():
    print(f'\n{nombre_app} - {version_app}')
    print(f'{"=" * (len(nombre_app) + len(version_app) + 3)}\n')

    correo = solicitar_correo('Correo: ')
    usuario = usuario_por_correo(correo)

    if usuario:
        contrasenia = solicitar_contrasenia('Contrasena: ')
        if bcrypt.checkpw(
            contrasenia.encode('utf-8'),
            usuario.contrasena.encode('utf-8')
        ):
            if usuario.activo:
                print(f'Bienvenido {usuario.nombre}. Rol: {usuario.rol}')
                cargar_menu(usuario)
            else:
                print('Usuario deshabilitado...')
        else:
            print('Contrasena erronea...')
    else:
        print('Usuario NO encontrado.\nIngrese nuevamente...')


def iniciar_aplicacion():
    while True:
        login_usuario()


iniciar_aplicacion()

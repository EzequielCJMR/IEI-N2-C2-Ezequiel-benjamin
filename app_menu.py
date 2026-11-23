from presentacion.presentacion_usuarios import login
from presentacion.menu import cargar_menu


flag= True

def main():
    while not login():
        print("Intente iniciar sesión nuevamente.")

    cargar_menu()


if __name__ == "__main__":
    main()



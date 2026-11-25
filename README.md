# Integrantes: 
# Ezequiel Muñoz 
# Benjamin Carmona



# Sistema de Encuestas - POO

Aplicación de consola desarrollada con Python, Peewee y MySQL. Gestiona usuarios,
administradores, encuestados, categorías y encuestas.

## Arquitectura

El proyecto mantiene responsabilidades separadas:

- `auxiliares`: validaciones, configuración y opciones de menú.
- `datos`: conexión, modelos ORM y repositorios.
- `negocio`: reglas del sistema y procesamiento.
- `presentacion`: interacción y formularios por consola.

La presentación no accede directamente a modelos ni repositorios; comunica los
datos solicitados al usuario con la capa de negocio.

## Dependencias

Python 3.12 o superior y MySQL Server.

```powershell
python -m pip install -r requirements.txt
```

## Configuración de MySQL

Para una instalación nueva, ejecuta los scripts dentro de `datos/sql/` en este
orden:

1. `2026.11.23_19.30_SETUP_COMPLETO.sql` — crea la base `encuestapru`, el
   usuario de aplicación y las tablas.
2. `2026.09.21.17.44_inserts_base_dato.sql` — carga los datos de prueba.

Importante:

- Ejecuta los scripts desde MySQL Workbench o phpMyAdmin como usuario con
  permisos administrativos.
- Ejecuta los inserts una sola vez y sólo si las tablas están vacías. No vuelvas
  a ejecutar ambos scripts sobre una base que ya contiene los datos de prueba.
- El usuario de aplicación mantiene `SELECT`, `INSERT`, `UPDATE` y `DELETE`
  únicamente sobre `encuestapru`.
- Si el usuario de aplicación ya existía en el servidor, confirma que su
  contraseña coincida con la configurada en `.env`; `CREATE USER IF NOT EXISTS`
  no cambia la contraseña de un usuario existente.

Configura `.env` en la raíz:

```dotenv
db=encuestapru
host=localhost
port=3306
user=ezequielmr
password=clave123
```

Copia `.env.example` a `.env`. Puedes cambiar `ezequielmr` y `clave123`
por tus propias credenciales, siempre que el usuario exista y tenga los
permisos sobre `encuestapru` indicados en los scripts.

No uses cuentas administrativas desde la aplicación.

## Ejecución

La ejecucion comienza en [app.py](/C:/Users/ezequ/gitmio/IEI-N2-C2-Ezequiel-benjamin/app.py),
siguiendo el mismo patrón del proyecto del profesor:

```powershell
python app.py
```

El programa solicita credenciales antes de abrir el menú. Las contraseñas se
ocultan en consola y se almacenan con Bcrypt.


## CRUD

- Usuarios: crear, listar, buscar, modificar y desactivar.
- Administradores: crear, listar, buscar, modificar y desactivar.
- Encuestados: crear, listar, buscar, modificar y desactivar.
- Categorías: crear, listar, buscar, modificar y eliminar.
- Encuestas: crear, listar, buscar, modificar y eliminar.

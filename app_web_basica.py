import bcrypt
from flask import Flask, render_template, request, redirect, url_for, session
from datos.modelos.usuario import Usuario

app = Flask(__name__)
app.secret_key = 'mi_clave_super_secreta_para_la_sesion'

@app.route('/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST']) # type: ignore
def procesar_login():
    # Usamos str() para que Pylance sepa que no es None
    email = str(request.form.get('email'))
    password = str(request.form.get('password'))

    usuario = Usuario.get_or_none(Usuario.email == email)

    if usuario:
        # Comparar contraseña con el hash
        password_bytes = password.encode('utf-8')
        hash_bytes = usuario.contrasena.encode('utf-8')
        
        if bcrypt.checkpw(password_bytes, hash_bytes):
            # Verificamos que esté activo
            if usuario.activo:
                session['usuario_id'] = usuario.id_usuario
                session['usuario_nombre'] = usuario.nombre
                session['usuario_rol'] = usuario.rol

                if usuario.rol == 'Administrador':
                    return redirect(url_for('panel_admin'))
                elif usuario.rol == 'Encuestado':
                    return redirect(url_for('panel_encuestado'))
            else:
                return render_template('error.html', mensaje="Cuenta desactivada.")
        else:
            return render_template('error.html', mensaje="Contraseña incorrecta.")
    else:
        return render_template('error.html', mensaje="El correo no está registrado.")

@app.route('/admin', methods=['GET'])
def panel_admin():
    if 'usuario_rol' in session and session['usuario_rol'] == 'Administrador':
        return render_template('admin.html', nombre=session['usuario_nombre'])
    return render_template('error.html', mensaje="Acceso denegado.")

@app.route('/encuestado', methods=['GET'])
def panel_encuestado():
    if 'usuario_rol' in session and session['usuario_rol'] == 'Encuestado':
        return render_template('encuestado.html', nombre=session['usuario_nombre'])
    return render_template('error.html', mensaje="Acceso denegado.")

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
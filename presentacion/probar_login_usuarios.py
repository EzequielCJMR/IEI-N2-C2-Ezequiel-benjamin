import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import tkinter as tk
from tkinter import messagebox
from datos.modelos.usuario import Usuario


def intentar_login():
    email = entry_email.get().strip()
    password = entry_pass.get().strip()

    # Buscamos en la base de datos
    usuario = Usuario.get_or_none((Usuario.email == email) & (Usuario.contrasena == password))

    if usuario:
        if usuario.activo: # Verificamos que no esté desactivado
            messagebox.showinfo("Éxito", f"¡Bienvenido {usuario.nombre}!\nRol: {usuario.rol}")
            ventana.destroy() # Cierra la ventana si el login es correcto
        else:
            messagebox.showerror("Error", "Este usuario está desactivado.")
    else:
        messagebox.showerror("Error", "Email o contraseña incorrectos.")

# Ventana
ventana = tk.Tk()
ventana.title("Login - Sistema de Encuestas")
ventana.geometry("350x250")

# Título
tk.Label(ventana, text="Iniciar Sesión", font=("Arial", 16, "bold")).pack(pady=20)

# Campo Email
tk.Label(ventana, text="Email:").pack()
entry_email = tk.Entry(ventana, width=30)
entry_email.pack(pady=5)

# Campo Contraseña (con asteriscos)
tk.Label(ventana, text="Contraseña:").pack()
entry_pass = tk.Entry(ventana, width=30, show="*")
entry_pass.pack(pady=5)

# Botón
tk.Button(ventana, text="Ingresar", command=intentar_login, bg="#3498db", fg="white", width=15).pack(pady=20)

ventana.mainloop()
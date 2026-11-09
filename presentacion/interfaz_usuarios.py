import sys
import os
# Esto le dice a Python que agregue la carpeta raíz a su ruta de búsqueda
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from tkinter import ttk, messagebox
# Ahora sí encontrará el módulo negocio
from negocio.negocio_usuarios import procesar_listado_usuarios,procesar_listado_usuarios 

def mostrar_ventana_usuarios():
    # 1. Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Sistema de Encuestas - Usuarios")
    ventana.geometry("800x400")
    ventana.configure(bg="#f0f0f0")

    # 2. Título
    titulo = tk.Label(ventana, text="Listado de Usuarios", font=("Arial", 16, "bold"), bg="#f0f0f0")
    titulo.pack(pady=10)

    # 3. Crear la tabla (Treeview)
    # Definimos las columnas
    columnas = ("ID", "Nombre", "Email", "RUT", "Rol")
    tabla = ttk.Treeview(ventana, columns=columnas, show="headings", height=15)

    # Configurar los encabezados y el ancho de las columnas
    tabla.heading("ID", text="ID")
    tabla.column("ID", width=50, anchor="center")
    
    tabla.heading("Nombre", text="Nombre")
    tabla.column("Nombre", width=200)
    
    tabla.heading("Email", text="Email")
    tabla.column("Email", width=200)
    
    tabla.heading("RUT", text="RUT")
    tabla.column("RUT", width=120)
    
    tabla.heading("Rol", text="Rol")
    tabla.column("Rol", width=100)

    tabla.pack(fill="both", expand=True, padx=20, pady=10)

    # 4. Cargar los datos desde tu base de datos
    try:
        usuarios = procesar_listado_usuarios() # Llamamos a tu función existente
        
        if not usuarios:
            messagebox.showinfo("Información", "No hay usuarios registrados.")
        else:
            # Insertamos cada usuario en la tabla
            for user in usuarios:
                # Nota: Usamos el nombre de los campos de tu modelo (id_usuario, nombre, etc.)
                tabla.insert("", "end", values=(user.id_usuario, user.nombre, user.email, user.rut, user.rol))
    except Exception as e:
        messagebox.showerror("Error", f"Error al cargar datos:\n{e}")

    # 5. Botón para cerrar
    btn_cerrar = tk.Button(ventana, text="Cerrar Ventana", command=ventana.destroy, bg="#e74c3c", fg="white", font=("Arial", 10, "bold"))
    btn_cerrar.pack(pady=10)

    # 6. Ejecutar la ventana
    ventana.mainloop()

# Ejecutar la función
if __name__ == "__main__":
    mostrar_ventana_usuarios()
import tkinter as tk
from implementacion import *

ventana = tk.Tk()
ventana.title("PoliDelivery - EPN")
ventana.geometry("420x350")


def limpiar_ventana():
    for widget in ventana.winfo_children():
        widget.destroy()

def menu_Principal():
    limpiar_ventana()
    tk.Label(ventana, text="MENÚ PRINCIPAL", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Button(ventana, text="Registrarse", width=25, command=registrar).pack()
    tk.Button(ventana, text="Iniciar Sesión", width=25, command=iniciar_seccion).pack()
    tk.Button(ventana, text="Iniciar como Admin", width=25, command=iniciar_admin).pack()

def registrar():
    limpiar_ventana()
    global correo_registrar, password_registrar

    correo_registrar = tk.Entry(ventana)
    password_registrar = tk.Entry(ventana)

    correo_registrar.pack()
    password_registrar.pack()

    tk.Button(ventana, text="Registrar", command=guardar_user).pack()
    tk.Button(ventana, text="Volver", command=menu_Principal).pack()


def guardar_user():
    with open("registros.txt", "a") as archivo:
        archivo.write(correo_registrar.get() + "|" + password_registrar.get() + "\n")

def iniciar_seccion():
    limpiar_ventana()
    global seccion_correo, seccion_password

    seccion_correo = tk.Entry(ventana)
    seccion_password = tk.Entry(ventana)

    seccion_correo.pack()
    seccion_password.pack()

    tk.Button(ventana, text="Iniciar Sesión", command=leer_user).pack()
    tk.Button(ventana, text="Volver", command=menu_Principal).pack()


def leer_user():
    with open("registros.txt", "r") as archivo:
        for linea in archivo:
            correo, password = linea.strip().split("|")
            if correo == seccion_correo.get() and password == seccion_password.get():
                menu_User()
                return

def iniciar_admin():
    limpiar_ventana()
    global admin_correo, admin_password

    admin_correo = tk.Entry(ventana)
    admin_password = tk.Entry(ventana)

    admin_correo.pack()
    admin_password.pack()

    tk.Button(ventana, text="Entrar como Admin", command=leer_admin).pack()
    tk.Button(ventana, text="Volver", command=menu_Principal).pack()


def leer_admin():
    with open("Admins.txt", "r") as archivo:
        for linea in archivo:
            correo, password = linea.strip().split("|")
            if correo == admin_correo.get() and password == admin_password.get():
                menu_admin()
                return

def menu_admin():
    limpiar_ventana()
    global origen, destino, distancia

    tk.Label(ventana, text="ADMIN - AGREGAR RUTA", font=("Arial", 13, "bold")).pack(pady=5)

    origen = tk.Entry(ventana)
    destino = tk.Entry(ventana)
    distancia = tk.Entry(ventana)

    origen.insert(0, "Origen")
    destino.insert(0, "Destino")
    distancia.insert(0, "Distancia (km)")

    origen.pack()
    destino.pack()
    distancia.pack()

    tk.Button(ventana, text="Guardar Ruta", command=guardar_ruta).pack(pady=5)
    tk.Button(ventana, text="Volver", command=menu_Principal).pack()


def guardar_ruta():
    agregar_ruta(origen.get(), destino.get(), distancia.get())
    tk.Label(ventana, text="Ruta guardada y centro añadido al árbol").pack()

def menu_User():
    limpiar_ventana()
    global origen, destino

    tk.Label(ventana, text="USUARIO - CALCULAR ENVÍO", font=("Arial", 13, "bold")).pack(pady=5)

    origen = tk.Entry(ventana)
    destino = tk.Entry(ventana)

    origen.insert(0, "Origen")
    destino.insert(0, "Destino")

    origen.pack()
    destino.pack()

    tk.Button(ventana, text="Calcular Costo", command=mostrar_costo).pack(pady=5)
    tk.Button(ventana, text="Volver", command=menu_Principal).pack()


def mostrar_costo():
    costo = calcular_costo(origen.get(), destino.get())
    if costo is None:
        tk.Label(ventana, text="Ruta no disponible").pack()
    else:
        tk.Label(
            ventana,
            text=f"Costo total: ${costo:.2f}",
            font=("Arial", 12, "bold")
        ).pack()

if __name__ == "__main__":
    menu_Principal()
    ventana.mainloop()

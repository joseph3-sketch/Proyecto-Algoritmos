import tkinter as tk
from implementacion import *
import re
from tkinter import messagebox
import os

ventana = tk.Tk()
ventana.title("PoliDelivery - EPN")
ventana.geometry("420x350")


def limpiar_ventana():
    for widget in ventana.winfo_children():
        widget.destroy()

def menu_Principal():
    limpiar_ventana()
    tk.Label(ventana, text="MENÚ PRINCIPAL", font=("Arial", 14, "bold")).pack()
    tk.Button(ventana, text="Registrarse", width=25, command=menu_registrar).pack()
    tk.Button(ventana, text="Iniciar Sesión", width=25, command=menu_iniciar_seccion).pack()
    tk.Button(ventana, text="Iniciar como Admin", width=25, command=menu_iniciar_admin).pack()

def menu_registrar():
    limpiar_ventana()
    global correo_registrar, password_registrar,nombre_registrar,identificador_registrar,edad_registrar
    
    nombre_registrar = tk.Entry(ventana) 
    tk.Label(text="Ingrese su nombre").pack()
    nombre_registrar.pack()
    
    identificador_registrar = tk.Entry(ventana) 
    tk.Label(text="Ingrese un identificador").pack()
    identificador_registrar.pack()
    
    edad_registrar = tk.Entry(ventana) 
    tk.Label(text="Ingrese su edad").pack()
    edad_registrar.pack()
    
    correo_registrar = tk.Entry(ventana) 
    tk.Label(text="Ingrese un correo").pack()
    tk.Label(text="\n").pack
    
    password_registrar = tk.Entry(ventana,show="*") 
    correo_registrar.pack()
    tk.Label(text="Ingrese una contraseña").pack()
    password_registrar.pack()

    tk.Button(ventana, text="Registrar", command=guardar_user_en_registros).pack()
    tk.Button(ventana, text="Volver", command=menu_Principal).pack()


def guardar_user_en_registros():
    corre = correo_registrar.get()
    password = password_registrar.get()
    if not corre.endswith("@gmail.com"):
        messagebox.showerror("Error","Correo invalido, ingrese al final @gmail.com")
        return
    patron_password = r"^(?=.*[A-Z])(?=.*\d).+$"
    if not re.match(patron_password, password):
        messagebox.showerror("Error", "La contraseña debe tener al menos una mayúscula y un número")
        return

    with open("registros.txt", "a") as archivo:
        archivo.write(correo_registrar.get() + "|" + password_registrar.get() + "\n")
    
    with open("usuarios.txt","a") as archivos_user:
        archivos_user.write(nombre_registrar.get()+"|"+identificador_registrar.get()+"|"+edad_registrar.get()+"|"+correo_registrar.get()+"|"+password_registrar.get()+"\n")
        

def menu_iniciar_seccion():
    limpiar_ventana()
    global seccion_correo, seccion_password
    seccion_correo = tk.Entry(ventana)
    seccion_password = tk.Entry(ventana,show="*")
    tk.Label(text="Ingrese su correo").pack()
    seccion_correo.pack()
    
    tk.Label(text="Ingrese su contraseña").pack()
    seccion_password.pack()
    tk.Button(ventana, text="Iniciar Sesión", command=leer_user).pack()
    tk.Button(ventana, text="Volver", command=menu_Principal).pack()


def leer_user():
    global seccion_password,guardar_correo
    with open("registros.txt", "r") as archivo:
        for linea in archivo:
            correo, password = linea.strip().split("|")
            if correo == seccion_correo.get() and password == seccion_password.get():
                guardar_correo = correo
                menu_User()
                return
        return  messagebox.showerror("Error", "correo o contraseña incorrecta")

def menu_iniciar_admin():
    limpiar_ventana()
    global admin_correo, admin_password
    admin_correo = tk.Entry(ventana)
    admin_password = tk.Entry(ventana,show="*")
    tk.Label(text="Ingrese su correo").pack()
    admin_correo.pack()
    tk.Label(text="Ingrese su contraseña").pack()
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
    tk.Label(ventana, text="--- Agregar Ruta ---").pack()
    origen.insert(0, "Origen")
    destino.insert(0, "Destino")
    distancia.insert(0, "Distancia (km)")
    origen.pack()
    destino.pack()
    distancia.pack()
    tk.Button(ventana, text="Guardar Ruta", command=guardar_ruta).pack(pady=5)
    
    # Nuevas opciones
    tk.Label(ventana, text="--- Gestión de Centros ---").pack(pady=5)
    tk.Button(ventana, text="Actualizar Nombre de Centro", width=25,bg="#28a745", fg="white", command=ventana_actualizar).pack(pady=2)
    tk.Button(ventana, text="Eliminar Centro", width=25, command=ventana_eliminar, bg="red").pack(pady=2)
    
    tk.Button(ventana, text="Volver al Menú Principal", command=menu_Principal).pack(pady=10)

def guardar_ruta():
    agregar_ruta(origen.get(), destino.get(), distancia.get())
    tk.Label(ventana, text="Ruta guardada").pack()
    tk.Label(ventana, text=f"Ruta {origen.get()} a {destino.get()}").pack()
    #guardar en archivos centros:
    with open("centros.txt","a") as archivo:
        archivo.write(origen.get()+"|"+destino.get()+"|"+distancia.get()+"\n")

def menu_User():
    limpiar_ventana()
    global origen, destino
    tk.Label(ventana, text="USUARIO - CALCULAR ENVÍO", font=("Arial", 13, "bold")).pack(pady=5)
    origen = tk.Entry(ventana)
    destino = tk.Entry(ventana)
    tk.Label(text="Origen").pack()
    origen.pack()
    tk.Label(text="Destino").pack()
    destino.pack()
    tk.Button(ventana, text="Calcular Costo", command=mostrar_costo).pack(pady=5)
    
    ingrese_region = tk.Entry(ventana)
    tk.Label(text="ingrese una region para listar sus centros disponibles").pack(pady=5)
    ingrese_region.pack()
    tk.Button(ventana, text="listar centros disponibles", bg="#17a2b8",command=lambda:ver_centros(arbol_logistico,ingrese_region.get().capitalize())).pack(pady=5)
    #inplemetar el ver regiones disponibles
    tk.Button(ventana, text="Volver", command=menu_Principal).pack()
    
    tk.Label(text="-----------------------------------------------------").pack(pady=5)
    tk.Label(text="Para confirmar el envio de click al button (Enviar paquete)").pack(pady=5)
    tk.Button(ventana, text="Confirmar y Registrar Envío", command=registrar_envio, bg="#28a745", fg="white").pack(pady=5)



def mostrar_costo():
    costo = calcular_costo(origen.get(), destino.get())
    if costo is None:
        tk.Label(ventana, text="Ruta no disponible").pack()
    else:
        tk.Label(
            ventana,
            text=f"Costo total de {origen.get()} hasta {destino.get()} es: ${costo:.2f}",
        ).pack()



def ver_centros(arbol, region_ingresada):
    regiones = arbol.get("regiones", {})
    if region_ingresada in regiones:
        lista_centros = regiones[region_ingresada]
        mensaje = "\n".join([f"- {centro}" for centro in lista_centros])
        messagebox.showinfo(f"Centros en {region_ingresada}", mensaje)
    else:
        messagebox.showwarning("No encontrado", f"La región '{region_ingresada}' no existe en el sistema.")
      
def ventana_eliminar():
    # Ventana emergente simple
    top = tk.Toplevel(ventana)
    top.title("Eliminar Centro")
    top.geometry("300x150")
    
    tk.Label(top, text="Nombre del centro a eliminar:").pack(pady=5)
    entrada_del = tk.Entry(top)
    entrada_del.pack()

    def confirmar_eliminacion():
        centro = entrada_del.get()
        if eliminar_centro_sistema(centro):
            messagebox.showinfo("Éxito", f"Centro '{centro}' eliminado correctamente.")
            top.destroy()
        else:
            messagebox.showerror("Error", "El centro no existe.")

    tk.Button(top, text="Eliminar Definitivamente", command=confirmar_eliminacion, bg="red", fg="white").pack(pady=10)

def ventana_actualizar():
    top = tk.Toplevel(ventana)
    top.title("Actualizar Centro")
    top.geometry("300x200")
    
    tk.Label(top, text="Nombre actual:").pack()
    antiguo_ent = tk.Entry(top); antiguo_ent.pack()
    
    tk.Label(top, text="Nombre nuevo:").pack()
    nuevo_ent = tk.Entry(top); nuevo_ent.pack()

    def confirmar_actualizacion():
        antiguo = antiguo_ent.get()
        nuevo = nuevo_ent.get()
        if actualizar_centro_sistema(antiguo, nuevo):
            messagebox.showinfo("Éxito", f"Se actualizó {antiguo} a {nuevo}")
            top.destroy()
        else:
            messagebox.showerror("Error", "No se pudo actualizar (nombre no encontrado o nuevo nombre ya existe)")

    tk.Button(top, text="Actualizar", command=confirmar_actualizacion).pack(pady=10)

            
def registrar_envio():
    costo = calcular_costo(origen.get(), destino.get())

    if costo is None:
        messagebox.showerror("Error", "No existe una ruta válida para registrar.")
        return

    with open("rutas-nombre-del-cliente.txt", "a") as archivo:
        linea = f"{guardar_correo}|{origen.get().capitalize()}|{destino.get().capitalize()}|{costo:.2f}\n"
        archivo.write(linea)
    messagebox.showinfo("Éxito", "Envío registrado correctamente. ¡Gracias por usar el sistema!")


if __name__ == "__main__":
    menu_Principal()
    ventana.mainloop()



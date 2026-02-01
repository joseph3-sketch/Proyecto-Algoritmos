import tkinter as tk
import os

ventana = tk.Tk()
ventana.title("PoliDelivery - EPN")
ventana.geometry("400x300")

def limpiar_ventana():
    for widget in ventana.winfo_children():
        widget.destroy()
        
def menu_Principal():
    limpiar_ventana()
    tk.Label(ventana, text="MENÚ PRINCIPAL", font=("Arial", 12, "bold")).pack()
    tk.Button(ventana, text="Registrarse", width=20, command=registrar).pack()
    tk.Button(ventana, text="Iniciar Sesión", width=20, command=iniciar_seccion).pack()
    tk.Button(ventana, text="Iniciar como Admin", width=20, command=iniciar_admin).pack()

def registrar():
    limpiar_ventana()
    global correo_registrar,password_registrar
    correo_registrar = tk.Entry(ventana)
    correo_registrar.pack()
    password_registrar= tk.Entry(ventana)
    password_registrar.pack()
    tk.Button(ventana,text="registrar", command=guardar_user).pack()
    tk.Button(ventana, text="Volver", command=menu_Principal).pack()

def guardar_user():
    correo_R_guardar = correo_registrar.get()
    password_R_guardar = password_registrar.get()
    with open("C:/Users/SJ-Jo/Desktop/deberes_2025b/algoritmos/Nueva carpeta/proyectoAlgoritmos/registros.txt","a") as archivo:
        archivo.write(correo_R_guardar +"|"+password_R_guardar+"\n")

def iniciar_seccion():
    limpiar_ventana()
    global seccion_correo,seccion_passsword
    seccion_correo = tk.Entry(ventana)
    seccion_correo.pack()
    seccion_passsword = tk.Entry(ventana)
    seccion_passsword.pack()
    tk.Button(ventana,text="iniciar seccion",command=leer_user).pack()
    tk.Button(ventana, text="Volver", command=menu_Principal).pack()
    
def leer_user():
    leer_correo = seccion_correo.get()
    leer_password = seccion_passsword.get()
    encontrado = False
    with open("C:/Users/SJ-Jo/Desktop/deberes_2025b/algoritmos/Nueva carpeta/proyectoAlgoritmos/registros.txt","r") as archivo:
        for i in archivo:
            correo,password =i.strip().split("|")
            if correo == leer_correo and password == leer_password:
                encontrado =True
                if encontrado is True:
                    print("se inicio seccion correctamente")
    if not encontrado:
        print("no se encontro al user")

def iniciar_admin():
    limpiar_ventana()
    global admin_correo,admin_passsword
    admin_correo = tk.Entry(ventana)
    admin_correo.pack()
    admin_passsword = tk.Entry(ventana)
    admin_passsword.pack()
    tk.Button(ventana,text="iniciar seccion",command=leer_admin).pack()
    tk.Button(ventana, text="Volver", command=menu_Principal).pack()
    
def leer_admin():
    leer_admin_correo = admin_correo.get()
    leer_admin_password = admin_passsword.get()
    encontrado = False
    with open("C:/Users/SJ-Jo/Desktop/deberes_2025b/algoritmos/Nueva carpeta/proyectoAlgoritmos/Admins.txt","r") as archivo:
        for i in archivo:
            correo,password =i.strip().split("|")
            if correo == leer_admin_correo and password == leer_admin_password:
                encontrado =True
                if encontrado is True:
                    limpiar_ventana()
                    menu_admin()
                    
    if not encontrado:
        exit()

def menu_admin():
    global origen,destino,distancia,precio 
    origen = tk.Entry(ventana)
    destino = tk.Entry(ventana)
    distancia = tk.Entry(ventana)
    precio = tk.Entry(ventana)
    origen.insert(0,"ingrese el origen")
    destino.insert(0,"ingrese el destino")
    distancia.insert(0,"ingrese la distancia")
    precio.insert(0,"ingrese el precio")
    origen.pack()
    destino.pack()
    distancia.pack()
    precio.pack()
    tk.Button(ventana,text="guardar centro",command=guardar_centros).pack()
    tk.Button(ventana, text="Volver", command=menu_Principal).pack()  

def guardar_centros():
    origen_centro=origen.get()
    destino_centro=destino.get()
    distancia_centro=distancia.get()
    precio_centro=precio.get()
    with open("C:/Users/SJ-Jo/Desktop/deberes_2025b/algoritmos/Nueva carpeta/proyectoAlgoritmos/centros.txt","a") as archivos:
        archivos.write(origen_centro +"|"+destino_centro+"|"+distancia_centro+"|"+precio_centro+"\n")

if __name__ == "__main__":
    menu_Principal()
    ventana.mainloop()
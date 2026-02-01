
#from menus_registros_inicio import *
arbol_logistico = {
    "nombre": "Ecuador",
        "regiones": {
            "Costa": {
                "Centros": {"Guayaquil":None, 
                            "Manta":None, 
                            "Esmeraldas":None,
                            }
            },
            "Sierra": {
                "Centros": {"Quito":None, 
                            "Cuenca":None, 
                            "Ambato":None,}
            },
            "Oriente": {
                "Centros": {"Tena":None, 
                            "El Coca":None}
            }
        }
}


def ver_centros(arbol,region_ingresada):
    regiones = arbol["regiones"]
    if region_ingresada in regiones:
        print(f"Centros de {region_ingresada}:")
        for centro in regiones[region_ingresada]["Centros"]:
            print(f"Para la region {region_ingresada} esta disponibles estos centros: {centro}")
    else:
        print("La región ingresada no existe")

ver_centros(arbol_logistico)

"""
if __name__ == "__main__":
    menu_Principal()
    ventana.mainloop()"""
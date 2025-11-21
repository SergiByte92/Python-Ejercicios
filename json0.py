
# Trabajar  con archivos JSON

import json
datos = {
    "nombre": "Carlos",
    "edad" : 25,
    "ciudad": "L'Hospitalet",
    "profesion": ["Programador", "currante", "youtube"],
    "disponibe": True,
    "altura": 2.55
}

with open ("datos.json","w", encoding="utf-8") as archivo:
    json.dump(datos, archivo,indent=4,ensure_ascii=False)

# LEER UN ARCHIVO JSON

with open ("datos.json","r", encoding="utf-8") as archivo:
    datos=json.load(archivo)
    print(datos)
    print (type(datos))

# Carga el  contenido de un archivo JSON en un diccionario

# Borrar un archivo
import os

if os.path.exists("virus.txt"):
    os.remove("virus.txt")
    print("archivo eliminado")
else:
    print("El archivo no existe")
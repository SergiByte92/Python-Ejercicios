# Un diccionario anidado es un diccionario dentro de otro diccionario

print (" DICCIONARIO  ANIDADO")

universidad = {
    "nombre": "iFP",
    "estudiantes": {
        "Carlos": {
            "ref":"CA2345",
            "edad": 24,
            "estudios": "DAM 1",
            "hobbies": ["nadar","domir","leer"]
        },
         "Maria": {
            "ref":"CA2385",
            "edad": 64,
            "estudios": "DAM 2",
            "hobbies": ["pintar","hacer yoga","salir de fiesta"]
        }
    }
}

# ¿ Qué estudios tiene Carlos?

print("Estudios de Carlos: ", universidad["estudiantes"]["Carlos"]["estudios"])
# Sacar por consola el segundo hobby que tiene Carlos
print("Hobbie de Carlos: ", universidad["estudiantes"]["Carlos"]["hobbies"][1])

# Sacar por consola el último hobby que tiene María

print(f"el último Hobbie de María es {universidad['estudiantes']["Maria"]["hobbies"][-1]}")

# Como puedo recorrer un diccionario anidado

print ("\n ------ Recorrer un diccionario anidado ----------")
for estudiante, info in universidad ["estudiantes"].items():
    print(f"\nEstudiante: {estudiante}")
    for clave, valor in info.items():
        print(f"{clave}: {valor}")
# Ejercicio 1: Crear un diccionario: estudiante con 3 llaves: nombre, edad, estudios. Imprime el diccionario

estudiante = {
    "nombre": "Maria",
    "edad": 22,
    "estudios": "DAM 1"
}
print(estudiante)

# Otra forma de crear un diccionario

otra_forma = dict(nombre = "Pepe Juan", edad = 128, ciudad = "Almeria", jubilado = "Sí")
print(otra_forma)

# Encontrar la longitud del diccionario (cúantas llaves-valor tiene)

print(f"La longitud del diccionario es: {len(estudiante)} elementos")
print(f"La longitud del otro diccionario es: {len(otra_forma)} elementos")

# Recorrer el diccionario: otra_forma  --> salga clave y valor

for clave, valor in otra_forma.items():
    print(f"{clave} y {valor}") # Imprimimos la clave y su valor

# Otra forma

for clave in otra_forma:
    print(f"{clave} -> {otra_forma[clave]}") 

print(" Acceso a los elementos del diccionario: ")
# print(estudiante[estudio])  ERROR: name 'estudio' is not defined

# print (estudiante.get[estudio]  ERROR: name 'estudio' is not defined


# Cómo puedo verificar si una llave (key) existe

if "edad" in estudiante:
    print ("Tiene edad regristrada")
else:
    print("No se encontró esta propiedad (key)")

# Modifica el diccionario estudiante, añadiento 3 pares llave-valor nuevas

estudiante["telefono"]= " 666 666 666"
estudiante["is Repetidor"]= "Sí"
estudiante["poblacion"]= " L'hospitalet"
estudiante["cp"] = "08904"

print(estudiante)

# Obtener listado de las llaves

for llave in estudiante.keys():
    print(f"Llave : {llave}")
print(f"Otra forma de obtener las llaves: {estudiante.keys()}")

# Obtener listado de los valores

for valor in estudiante.values():
    print(f"Valores: {valor}")

print(f"Otra forma de obtener las llaves: {estudiante.values()}")


# Obetener listado de las llaves-valores

for valor, llave in estudiante.item():
    print(f"Llave: {llave} -> {valor}")

# Eliminar la llave "cp"

# del estudiante("cp") # Dara error, tiene que ser con corchetes

# Eliminar (borrar) un diccionario

print(f"Antes de borrar el diccionario: ")
print(estudiante)
print(f"Borro el diccionario: ")
estudiante.clear()
print(estudiante) # {}
print (type (estudiante))

# ELIMINAR un diccionario, incluida la variable
del estudiante
print (type(estudiante)) # Error name 'estudiante' is not defined



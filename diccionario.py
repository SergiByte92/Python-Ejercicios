print("----- DICCIONARIOS -----")

# Creamos un diccionario de persona: clave y un valor

persona = {
    'nombre': 'encarni',
    'edad': 99,
    'ciudad': 'L\'Hospitalet'
}

# Imprimimos al diccionario

print (f"Diccionario de persona {persona}")

# Accedemos a los elementos del diccionario

print (f"Nombre: {persona['nombre']}")
print (f"Edad: {persona.get('edad')} años")
print (f"Edad: {persona.get('ciudad')} ")

# Modificamos los elementos del diccionario

persona['edad'] = 39 # Modificamos la edad

print (f"Diccionario de persona {persona}")

# Agregar un nuevo elemento al diccionario

persona['profesion'] = 'Programadora'
print(f"Diccionario de persona : {persona}")

# Eliminar un elemento

del persona ['ciudad']
print (f"Diccionario de persona {persona}")

profesion = persona.pop('profesion')
print (f"Diccionario de persona {persona}")
print (f"Profesion eliminada {profesion}")

# Recorrer los elementos de un diccionario (llave,valor)

for llave, valor in persona.items():
    print(f"Llave: {llave}, valor: {valor}")

# Obtener SÓLO los valores

print ("\nValores del diccionario: ")
print (f"Valor: {valor}")

# Obtener SÓLO las llaves

print ()
print (f"Las llaves del diccionario: ")
for llave in persona.key():
    print(f" Llave: {llave}")
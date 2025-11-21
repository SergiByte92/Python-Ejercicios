# Una función puede devolver VARIOS RESULTADOS

def persona_mayusculas (nombre, apellido, edad):
    print("Esta función devuelve VARIOS VALORES (tupla)")
    return nombre.upper(), apellido.upper(),edad

nombre, apellido,edad =persona_mayusculas ("Sandra","ramirez",99)
print(f"Resultado -> Persona: nombre= {nombre}, apellido = {apellido}, edad = {edad}")

# Se pueden asignar valores PREDETERMINADOS a los parametros

def saludar_persona(nombre="anonimo"):
    print(f"Bienvenido, {nombre}")

saludar_persona()
saludar_persona("Pepe luis")

def imprimir_persona(nombre="Joze Lui", apellido="tacata",edad= 111):
    print(f"Nombre : {nombre} Apellido {apellido} y edad {edad}")

imprimir_persona()
imprimir_persona(nombre="Carlos")
imprimir_persona(nombre="Carlos",apellido="Miau")
imprimir_persona(nombre="Carlos",apellido="Miau",edad=2)

def suma_total(*numeros): # Recibe CUALQUIER cantiad de argumentos
    return sum (numeros)
print(suma_total(2,3))
print(suma_total(2,3,4,5,6))

# Funciones con argumentos clase ( **Kwarks)

# Kwarks permite pasar MÚLTIPLES valores con nombre sin necesidad de definir varios parámetros

def mostrar_info(**datos): # Dos asteriscos : una clave y un valor
    for clave,valor in datos.items():
        print (f"{clave} -> {valor}")
    print("---------------------")

mostrar_info(nombre="Pepe", edad = 99, ciudad="Barcelona")
mostrar_info(nombre="Sandra", edad = 39, ciudad="Madrid", en_activo="si", cp="08980")

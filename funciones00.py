
""" FUNCIONES """

# Una función es un bloque de código REUTILIZABLE
# Ventajas

# REUTILIZABLE  Evita repetir código 
# MODULAR   Dividir el programa en bloque lógicos, una función hace sólo una cosa
# FACILIDAD MANTENIMIENTO: Cambiar una función SÓLO afecta a esa parte del código
# MEJORA LA LEGIBILIDAD: El código es más fácil de entender

def saludar ():
    print ("Hola Mundo!")

# Llamo a la función (utilizo la función), INVOCO a la función

def saludar_persona(nombre): # Función que acepta UN PARÁMERTRO (variable que recibe una función
    print (f"Hola {nombre}")

saludar_persona("Olga") # le paso un ARGUMENTO (valor real que paso a una función)

# Realizar una función que sume dos números

def suma(a,b):
    return a+b

x,y=2,3

print(f"La suma de {x} + {y} es {suma(x,y)}")

# Ejercicio: Realizar una función que me diga si un número es par o impar
# La función se llamará: es_par
# árgumentos: numero
# Devuelve: "Par" o "Impar"

"""def es_par(x):
    if x%2==0:
        print(f"El número {x} es par")
    else:
        print(f"El número {x} es impar ")                  

par(2)  
"""
# Otra manera

def es_par(numero):
    if x%2==0:
        return "Par"
    return "impar"

num = int (input("Introduce un número"))
print(f"El número {num} es {es_par(num)}")

# Realizar una función que divida dos números
# La función se llamará : dividir Aceptará DOS parámetros : a, b

def dividir (a,b):
    return a/b
x = int (input(" Introduce un número entero: "))
y = int (input(" Introduce un número entero: "))

print (f"La división entre {x} y {y} es igual a {dividir(x,y)}")
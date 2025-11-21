# Ejercicio 1:
# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre por pantalla cada elemento de la lista junto con su cuadrado

import random

# Genero lista



numeros= [random.randint(1,10) for _ in range(10)]

print(numeros)

for n in numeros:
    print(f"Número: {n:4} | Cuadrado: {n**2:4} | Cubo: {n**3:4}") # Los :3 es para reservar espacios

# Ejercicio 2
# Dada la siguiente lista  'números' imprimir cada elemento al cuadrado de la lista

numeros=[ 1,2,3,4,5]
cuadrados=[x**2 for x in numeros]

print(cuadrados)

# Ejercicio 3 ¿Qué hace el siguiente programa?
numeros=range(10+1)
pares = [x for x in numeros if x % 2==0]
print(pares)
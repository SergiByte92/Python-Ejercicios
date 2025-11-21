# ? Ejercicio 2: Mostrar índices y valores

# Dada la siguiente lista:

# colores = ["rojo", "verde", "azul", "amarillo"]

# Escribe un programa que muestre cada color junto con su posición en la lista.

colores = ["rojo", "verde", "azul", "amarillo"]

for indice,color in enumerate(colores):
    print(f"Indice {indice}: {color} ")



# ? Ejercicio 4: Sumar los elementos de una lista

# Dada la lista de números:

# valores = [3, 7, 2, 9, 1]

# Escribe un programa que calcule la suma total de los elementos de la lista y la muestre en pantalla.

valores = [3, 7, 2, 9, 1]
suma_total=sum(valores)
print(suma_total)

# Otra manera

suma_tot = 0  # Inicializamos la variable en 0

for numero in valores:
    suma_tot += numero  # Sumamos cada número de la lista a la variable

print(f"La suma total es: {suma_tot}")
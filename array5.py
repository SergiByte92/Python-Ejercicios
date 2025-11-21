# ? Ejercicio 5: Filtrar números pares

# Dada la lista:

# numeros = [12, 7, 5, 9, 16, 8, 3]

# Escribe un programa que genere una nueva lista con solo los números pares y la imprima.

numeros = [12, 7, 5, 9, 16, 8, 3]
pares=[]

for par in numeros:
    if par % 2 == 0:
        pares.append(par)
print(pares)


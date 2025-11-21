# ? Ejercicio 7: Contar cuántas veces aparece un elemento

# Dada la lista:

# letras = ["a", "b", "c", "a", "d", "b", "a", "c"]

# Escribe un programa que pregunte al usuario una letra y luego muestre cuántas veces aparece en la lista

# Utiliza el método count()

letras = ["a", "b", "c", "a", "d", "b", "a", "c"]

print(letras)

letra=input("\nIntroduzca una letra por favor: ")

if letra.isdigit():
    letra=input("\nDisculpe,pero tiene que introducir una letra por favor: ")

cantidad = letras.count(letra.lower().strip()) # No nos lo pide el cliente, pero , nos aseguramos que sea en minusculas para que coincida con la array,por otra parte, quitamos los espacios.

print(f"\nLa cantidad de veces que aparece la letra {letra.strip()} es de {cantidad} veces")

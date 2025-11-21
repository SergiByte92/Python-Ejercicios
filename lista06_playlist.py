# PLAYLIST

# Creamos una lista vacía

lista_reproduccion = []

numero_canciones = int (input("Cuántas canciones deseas agregar?: "))

for indice in range (numero_canciones):
    cancion = input(f"Proporciona la canción {indice+1}: ")
    lista_reproduccion.append(cancion)

# Ordenar la lista en orden alfabético
lista_reproduccion.sort()

# Mostrar las lista

for cancion in lista_reproduccion:
    print(f"{cancion}")


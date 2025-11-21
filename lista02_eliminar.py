# Eliminar elementos de una lista

lista = [1,2,3,2,4,5,6,7,8,9,10]

print(f"{lista} -> Lista original")

# Eliminar un SÓLO elemento de una lista. Método .remove(x)


lista.remove(2) # En el caso que haya varios repetidos, elimina el primero que encuentra
print(f"{lista} -> Se eliminó el número 2")

lista.remove(7)
print(f"{lista} -> Se eliminó el número 7")

# Eliminamos por ÍNDICE con el método pop(X)

lista.pop(1) # Elimino el elemento de la posición 1
print(f"{lista}")

# Eliminamos utilizando la palabra 'del'

del lista[4] # Elimino el elemento de la posición 4
print(f"{lista} -> Se eliminó el indice 4")

# Uitilizando slicing

del lista[5:]
print(f"{lista} -> Se eliminó los elementos desde el índice 5 en adelante")

# Obtener sublistas
sublistas = lista [2:4]

print(f"sublista [2:4]: {sublistas}")

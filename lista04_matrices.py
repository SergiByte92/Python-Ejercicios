matriz = [[10,2,3], [4,50,900],[7,800,10]] # Definimos una matriz 3 x 3

# Imprimimos matriz

for fila in matriz:
    print(fila)

print(f"El elemento en la segunda fila y tercera columna: {matriz[1][2]}") # fila 1 -> 4,50 y 900 y indice 2, el 900

# Imprimimos utilizando la funcion format

print ("\nOtra forma de imprimir una matriz ")

for fila in matriz:
    print("{:5d} {:5d} {:5d}".format(*fila))

print(f"Elemento en la segunda fila y tercera columna: {matriz[1][2]}")
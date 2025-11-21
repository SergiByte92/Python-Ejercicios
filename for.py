'''
    BUCLES O ITERACIONES
    range(start, stop, step)
    start --> valor inicial (opcional, por defecto 0)
    stop --> valor final (NO INCLUDE)
    step --> Incremento o decremento (opcional,por defecto vale 1)

'''

print("\nA.-")
for x in range(9):
    print(f"{x}", end=" ") # 0 1 ...8

print("\nB.-")
for x in range(1,5):
    print(f"{x}", end=" ") # 0 1 ...4

print("\nC.-")
for x in range(1,11,2):
    print(f"{x}", end=" ") # 1 3 5 7 9

print("\nD.-")
for x in range(-5,6,2):
    print(f"{x}", end=" ") # 1 3 5 7 9

print("\nE.-")
frutas=["Manzana", "Platano", "Pera"]

for cosas in frutas:
        print(f"{cosas}") # Imprime en pantalla la array en vertical


# Otra manera para ver su utilidad

"""
frutas = [("Manzana", 1.2), ("Platano", 0.5), ("Pera", 1.5)]

total = 0
for fruta, precio in frutas:
    total += precio # Suma al total el precio de cada fruta
    print(f"La {fruta} cuesta {precio}€.")

print(f"El costo total es {total}€.")

"""

              
for i in range (len(frutas)):   # En este caso el rango son los strings que hay, en este caso 3: 0 1 2
              print(f"{i} {frutas[i]}")
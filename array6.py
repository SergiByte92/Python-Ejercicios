# ? Ejercicio 6: Encontrar el número más grande

# Dada la lista:

# edades = [15, 22, 30, 18, 27, 35, 10]

# Escribe un programa que encuentre y muestre el número más grande de la lista, sin utilizar métodos

edades = [15, 22, 30, 18, 27, 35, 10]
mayor=float('-inf')   # si fuesen negativos, ya no funcionaria, por lo tanto, se inicializa en menos infinito

for num in edades:
    if mayor < num: 
        mayor = num # La variable toma un nuevo valor
print(mayor) 

menos_infinito = float('-inf')
print(menos_infinito)
print(type(menos_infinito))

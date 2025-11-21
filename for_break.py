print("BREAK")
for numero in range (1,10):
    if(numero%5==0):
        print(numero)
    break   # Salimos del bucle

print("Adiós")


for numero in range(1, 10):
    if(numero % 2 == 1):  # Si el número es impar
        continue  # Saltamos a la siguiente iteración
    print(numero)  # Si no es impar (es par), lo imprimimos

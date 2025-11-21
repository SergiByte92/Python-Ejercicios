
#! -------- LISTAS --------

lista = [1,2,3,4,5]

#? Imprimir listas
print(f"Lista original: {lista}")
print(f"type{lista}")

# ! La longitud de la lista
print (f"Nº de elementos de la lista:{len(lista)}")

# ! Acceder a los elementos de la lista
print (f"{lista[0]}")
print (f"{lista[1]}")
print (f"{lista[2]}")
print (f"{lista[3]}")

# ! Acceder al Último elemento de la lista: 
print(f"{lista[len(lista)-1]}")
print(f"{lista[-1]}")

# ! Invertir lista
lista.reverse()  # Primero invertimos
print(f"{lista} - Invertimos lista") # Luego mostramos

# print(f"{lista.reverse()"}) # Devuelve 'None'

print()
print("Listado de los elementos de la lista: ", end=" ")

for valor in lista:
    print (valor, end=" ")

 # ! Comprobar si un elento existe en la lista
# ? El 4 existe en la lista??

if 4 in lista:
        print('\nEl nº  pertenece en la lista')
else:
        print("\nEl nº no está en la lista")



# lista.sort()
# print(f"{lista}") # Imprimir por orden

# ! Otra forma de RECORRER una lista

frutas =['manza', 'pera', 'platano', 'uva']

for i in range(len(frutas)): 
    print(f"Índice {i} : {frutas[i]} ") # Imprimir indice y el valor --> mejor utilizar enumerate()

print()

# ! Metodo enumerate()
for i, fruta in enumerate(frutas):
    print(f"Índice {i} : {fruta} ")

# ! Metodo while

print("Metodo while")
print(f"Valor de i= {i}")
i=0


while i < len(frutas):
    print(frutas[i])
    i+=1

# ! Recorrer una lista en orden inverso

coches=["bmw", "mercedes", "toyota"]

# ? Forma 1: pista: [::-1]

for marca in coches[::-1]:
     print()
     print(marca)
# ? forma 2: reverse()
for marca in reversed(coches):
     print()
     print(marca, end=" ")
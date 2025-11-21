# Crear TUPLAS

# Crear una tupla

mi_tupla = (1,2,3,4)
print("Tupla: ", mi_tupla)

# Una tupla es una estructura ordenada de datos en  Python que permite una colección ordenada e INMUTABLE

# Acceder a un elemento de una tupla:

# print (f"Accedo al primer elemento de la tupa: {mi_tupla(0)}") Da ERROR

print (f"Accedo al primer elemento de la tupa: {mi_tupla[0]}") 
#mi_tupla[0] = 99
print(type(mi_tupla))

# Desempaquetar una tupla:
a, b, c, d = mi_tupla

print("Desempaqueto tupla", a,b,c,d)

a+=1
print(a)

#concatenacion

tupla1=(1,2,3)
tupla2=(4,5,6)

concatenacion = tupla1 + tupla2
print(concatenacion)

# Cálculo de la longitud de una tupla
print (f"La longitud de la tupla es: {tupla1} es {len(tupla1)} ")

# Contar ocurrencias de un elemento en una tupla
tupla3=(1,2,3,4,3,4,2,1,5,6)
print (f"Ocurrencias del nº3: {tupla3.count(3)}")

mi_lista = [10,20,30]
mi_tupla_desde_lista = tuple (mi_lista) # Convertimos una lista -->
print(type(mi_tupla_desde_lista))

# Convertir una tupla a lsita --> list()
mi_lista_desde_tupla = list(tupla3)
print(type(mi_lista_desde_tupla))

# Recorrer una tupla:
mi_tupla = ("rojo","naranja","verde")
for color in mi_tupla:
    print(color)

# Comparacion tuplas con listas

"""
# CARACTERÍSTICAS       TUPLA                       LISTA 

Mutabilidad             Inmutable                   Mutable


Sintaxis                (ele1,ele2)                 [ele1,ele2]

Rendimiento             Más rapido(por su inmu.)    Más lentas (por su muta)

Cuando utilizar...      Datos fijos                 Datos dinámicos            

"""
# Ejercicio 1 Crear una tupla con los números del 20 al 30 , mostrar la longitud de la tupla y el último elemento

tupla=(1,2,3)

print(f"La longitud de {tupla} es de {len(tupla)} y su ultimo elemento es {tupla[-1]}")

# Ejercicio 2 Crear una función que reciba una tupla y devuelva la SUMA de sus elementos

def sumatorio(tupla2):
    suma = 0
    for num in tupla2:
        suma += num
    return suma  # Devolver el resultado de la suma

tupla2=(2,4,6)
# Imprimir el resultado
print(sumatorio(tupla2))




    
# Ejercicio 3 Convierte una lista de nombres en una tupla y muestra el último nombre

tuplalista=tuple(tupla)

print(f"{tuplalista[-1]}")


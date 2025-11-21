#^ Ejercicio 1:

# Crea una función que retorne el máximo y el mínimo de una lista
numeros=[1,2,3,4,5,6,-77,8,-100]
def maximo_y_minimo(numeros):

  minimo=float('inf')
  maximo=float('-inf')

  for nums in numeros:
    if minimo > nums:
      minimo=nums
    if maximo < nums:
      maximo=nums
  return maximo, minimo
  
maximo,minimo=maximo_y_minimo(numeros)

print(f"Maximo: {maximo}")
print(f"Minimo: {minimo}")
"""

  

  return # Retorna ambos valores





lista = [3, 4, 8, 9, 4, 7]

resultado = maximo_y_minimo(lista)



if resultado:

  maximo, minimo = resultado

  print(f"Máximo: {maximo}, Mínimo: {minimo}") # Salida: Máximo: 9, Mínimo: 3

else:

  print("La lista está vacía")
















"""
#^ Ejercicio 2:

# Crear una función que retorne una lista con solo los números pares de la lista original.


lista2 = [2, 3, 4, 5, 6, 71, 54, 67, 88]

def filtrar_pares(lista):
    lista_pares = []  # Lista para almacenar los números pares
    for i in lista:
        if i % 2 == 0:
            lista_pares.append(i)  # Agregar los pares a la lista
    return lista_pares  # Retornar la lista de números pares

lista3 = filtrar_pares(lista2)  # Llamamos a la función
print(lista3)  # Mostramos el resultado


"""


#^ Ejercicio 3:

# Crear una función que elimine los elementos duplicados de la lista, manteniendo el orden original.


def eliminar_duplicados(lista):
    lista_sin_duplicados=[]
    for i in lista:
        if i not in lista_sin_duplicados:
            lista_sin_duplicados.append(i)
    return lista_sin_duplicados

  







lista = [3, 4, 8, 9, 4, 7, 3, 3,3 ]

print (f"Lista original: {lista}")

print(f"Lista sin repetidos: {eliminar_duplicados(lista)}")













#^ Ejercicio 4:



# Crear una función que cuente cuántos elementos son mayores que un valor dado.

def contar_mayores_que(array,num):
  
  contador=0
  for numeros in array:
        if num < numeros :
            contador +=1
  return contador
       
    







lista = [3, 4, 8, 9, 4, 7]

print(contar_mayores_que(lista, 5)) 

















#^ Ejercicio 5: 


def encontrar_indice(lista, elemento):
    for i in range(len(lista)):  # Recorremos la lista con el índice
        if lista[i] == elemento:  # Si encontramos el elemento
            return i  # Retornamos el índice de la primera ocurrencia
    return -1  # Si no encontramos el elemento, devolvemos -1

# Lista de ejemplo
lista = [3, 4, 8, 9, 4, 7]

# Llamada a la función y muestra del resultado
print(encontrar_indice(lista, 9))  # Debería imprimir el índice 3
print(encontrar_indice(lista, 5))  # Debería imprimir -1 porque el 5 no está en la lista














#^ Ejercicio 6:

# Crear una función que genere una nueva lista con el cuadrado de cada elemento.


def cuadrados(lista):
    listacuadrado=[]
    for nums in lista:
        cuadrado=nums**2
        listacuadrado.append(cuadrado)
    print(listacuadrado)


lista = [3, 4, 8, 9, 4, 7]

print(cuadrados(lista)) 


#^ Ejercicio 7:



# Crear la función 'promedio' que acceptará una lista y devolverá el valor promedio de esa lista con 3 decimales

# NO se puede utilizar el método sum()



def promedio(lista):
  
  divisor=len(lista)
  sumatorio=0
  for num in lista:
      sumatorio+=num  
  promedio_final=sumatorio/divisor
  
  return promedio_final



lista = [3, 4, 8, 9, 4, 7]

print(f"El promedio es:{promedio(lista):.3f}")















#^ Ejercicio 8:



# Crear una función que retorne un diccionario con la frecuencia (cuántas veces ha salido) de cada elemento.

def frecuencia_elementos(lista):
    frecuencia = {}  # Creamos un diccionario vacío
    for elemento in lista:
        if elemento in frecuencia:
            frecuencia[elemento] += 1  # Si el elemento ya está en el diccionario, aumentamos su contador
        else:
            frecuencia[elemento] = 1  # Si no está, lo agregamos con un contador de 1
    return frecuencia

# Ejemplo:

lista = [3, 4, 8, 9, 4, 7]

print(frecuencia_elementos(lista)) # Salida: {3:1, 4:2, 8:1, 9:1, 7:1}















#^ Ejercicio 9: Filtra elementos que son múltiplos de dos divisores diferentes



def filtrar_multiplos(lista, divisor1, divisor2):

    multiplos=[]

    for num in lista:
        if num % divisor1 == 0 and num % divisor2 == 0 :
            multiplos.append(num)
    return multiplos

  





lista = [10, 15, 20, 5, 3, 35, 40,50]

print (f"De la lista {lista}")

print("Los múltiplos de 2 y 5 son: ", filtrar_multiplos(lista, 2, 5)) """
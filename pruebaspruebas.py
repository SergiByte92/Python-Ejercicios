#^ Ejercicio 5: 

# Crear una función que retorne el índice de la primera ocurrencia de un elemento, o -1 si no existe


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


#^ Ejercicio 9: Filtra elementos que son múltiplos de dos divisores diferentes



def filtrar_multiplos(lista, divisor1, divisor2):

    multiplos=[]

    for num in lista:
        if num % divisor1 == 0 and num % divisor2 == 0 :
            multiplos.append(num)
    return multiplos

  





lista = [10, 15, 20, 5, 3, 35, 40,50]

print (f"De la lista {lista}")

print(f"Los múltiplos de 2 y 5 son: ", filtrar_multiplos(lista, 2, 5))

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
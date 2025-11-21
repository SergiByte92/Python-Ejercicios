# Separar en subcadenas (split)

datos = "Estais aburridos?"
lista= datos.split() # por defecto, separa cada elemento por ESPACIOS 

print(lista) 

usuario="Pedro Dominguez, 55, L'Hospitalet"

lista=usuario.split(",") #se genera una lista (array)
print(lista)
print(f"tu nombre es : {lista[0]}")
print(f"tienes es : {lista[1]} años")
print(f"vives en : {lista[2]}")
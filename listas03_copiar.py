# Defino una lista
a = [2,4,6,8,10]

# Diferentes formas de COPIAR una lista

b = a[:]
print(a)
print(b)

c=a.copy()
d= list(a) # list() constructor
print(f"Lista a: {a}")
print(f"Lista b: {b}")
print(f"Lista c: {c}")
print(f"Lista d: {d}")

# NOTA:
e=a # NO COPIA la lista,  sólo crea otra referencia (otro nombre) al mismo objeto
original= ['pera','manzana']
print(f"Lista original: {original}")
copia=original # ahora la lista tiene dos nombres: original y copia
print(f"Lista inicial: {original}")
print(f"Lista copia: {copia}")

# FORMA DE BORRAR LISTAS

# Borro la lista
del a
# print(f"Lista a: {a}") # Error porque ya no existe la variable a ni su contenido
                       # name 'a' is not defined
b.clear() # Borro los elementos de la lista b
print(f"Lista b: {b}")
c[:] = [] # Borro los elementos de la lista c
print(f"Lista c: {c}")
# c[]= []
print(f"Lista c: {c}")
d =[] # Asignamos a la lista 'd' una lista vacia
print(f"Lista d: {d}")



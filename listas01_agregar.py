
# !--------- AGREGAR ELEMENTOS A UNA LISTA ---------

lista =[1,2,3,4,5]
print(f"Lista original: {lista}")

# ? Puedo modificar los elementos de la lista (MUTABLE)
lista[0]=10

print(f"Lista original: {lista}")

# ! Agregar SÓLO UN nuevo elemento al final de la lista .append()

lista.append(6)
print(f"Lista modificada {lista}")

# ! Agregar VARIOS elementos al FINAL de la lista .extend()

lista.extend([2,3,4,5])
print(f"Lista modificada{lista}")

# ! También puedo utilizar el operador suma (CONCATENACIÓN)

lista = lista + [10, 11, 12]

# ! También puedo utilizar el operador suma para añadirlos al principio (CONCATENACIÓN)

lista= [10,11,12] + lista

# ! Agregar un elemento en un indice especifico .insert()

lista.insert(0,5)

print(f"Lista modificada {lista}")

frutas =[ 'manzana', 'peras', 'platanos','naranja']
elementos_a_insertar= ["rueda", "llave"]
posicion=1
for elemento in elementos_a_insertar[::-1]:
    frutas.insert(posicion,elemento)
print(frutas)
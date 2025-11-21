# Ejercicio 1

x = 10 # Defino una variable global
def imprimir_x():
    print(x) # Puedo acceder a la variable global PARA LEER

imprimir_x()

# Ejercicio 2
z = 99 # Global

def imprimir_z() :
    z=5   # Local
    print(z) 

imprimir_z()
print(z)

# Ejercicio 3 : MODIFICAR UNA VARIABLE GLOBAL

z=20
def modificar_z():
    z=30
    print("z dentro de la función",z)

modificar_z()
print("z fuera de la funcion",z)

# Ejercicio 4:

w = 40
def modificar_w():
    global w
    w += 1
    print("W dentro de la función",w)

modificar_w()
print("w fuera de la función",w)
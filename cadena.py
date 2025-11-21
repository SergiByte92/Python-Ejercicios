# cadenas en Python

cadena1="Hola mundo!"

cadena2= """ Python
                    no
                        me
                            parece tan complicado """

cadena3=""" Otra
    CADENA
        EN
            PYTHON """

print(cadena1)
print(cadena2)
print(cadena3)

#Acceder a un elemento de la cadena

cadena1="Hola mundo!"

print("Accedo al primer elemento de la cadena", cadena1[0]) #En este caso la H
print("Accedo a la M", cadena1[5]) #En este caso la M
print("Accedo al !", cadena1[10]) #En este caso la !
print("Accedo al !", cadena1[-1]) #En este caso la !
# print("Accedo al elemento 22", cadena1[22]) #En este caso IndexError: string index out of range

#Metodo de saber la longitud

print(f"La longitud de la cadena es: {len(cadena1)}") # 11

# Ejercicio: Acceder al ultimo elemento de la cadena, utilizando SOLO LA FUNCION LEN()
nombre="Juan Jose"
ultimo=len(nombre)
print(f"Acceder a la ultima letra de la cadena es: {nombre[ultimo-1]}")
#print(f"Acceder a la ultima letra de la cadena es: {nombre[ultimo]-1}") esta fuera de rango, ademas de intentar restar a una unidad
print(f"Acceder a la ultima letra de la cadena es: {nombre[-1]}")

#concatenacion de cadenas

nombre = " Sergi "
apellido = " Garcia "

concatenacion = nombre +" " + apellido

print(concatenacion)

#Utilizar el metodo join

concatenacion= ' '.join([nombre,apellido])
print(concatenacion)
concatenacion= ' '.join([nombre,' ',apellido])
print(concatenacion)

# f- strings

print(f"hola {nombre}, tu apellido  {apellido}")

#metodos de cadenas 
cadena= "hola mundo"
print(f"Cadena original: {cadena}")
print(f"Cadena en mayusculas : {cadena.upper()}") #convertir en mayusculas
print(f"Cadena en minusculas : {cadena.lower()}") #convertir en minusculas #ALT en un sitio y ALT en otro sitio y modificas a la vez
password="  1234    "
print(f'Tu contraseña es:{password.strip()}') # Elimina espacios iniciales y finales


ciudad= "       BarcElOnA"

print(f"Vives en : {ciudad.strip().lower()}")
print(f"Vives en : {ciudad.strip().lower()}")




"""
Ejercicio 1.- Escribe un programa que imprima los números del 1 al 10 utilizando el bucle for.
El resultado tiene que salir en una SOLA LINEA

Ejercicio 2.- Escribe un programa que imprima los números del 1 al 7 utilizando el bucle for.
El resultado tiene que salir en una SOLA LINEA

Ejercicio 3.- Haz un programa que pida al usuario que introduzca números. El programa los sumará hasta que introduzca un cero. 
Después mostrará la SUMA TOTAL

Ejercicio 4.- Escribe un programa que imprima sólo los numeros impares del 3 al 15

Ejercicio 5.- Escribe un programa que pida un número y muestre la tabla de multiplicar de ese número hasta el 10

Ejercicio 6.- Realiza un programa que genere un número aleatorio entre 1 y 10, el usuario tiene que intentar adivinarlo

Ejercicio 7.- Realiza un programa que genere un número aleatorio entre 1 y 10, el usuario tiene que intentar adivinarlo, sólo dispondra de 5 intentos. 
Este valor lo guardaremos en una CONSTANTE llamada vidas. Cada vez que el usuario introduzca un número, el programa le dirá si el número secreto es mayor o menor. Si el usuario acierta, gana el guejo. Si se queda sin intentos, pierde y el programa revelará el número secreto

"""

# Ejercicio 1

for i in range(1,11):
    print(i, end=" ")

# Ejercicio 2

for i in range(1,8):
    print(i, end=" ")

# Ejercicio 3

try:

    num=float(input("Introduzca un número: "))
    count=0

    while num !=0:
        
        count = count+num
        print(f"La suma total es de: {count}")
        
        num=float(input("Introduzca un número: "))
       
except ValueError:
    print("Introduzca correctamente el número")



# Ejercicio 4

for i in range(3,16,2):
    print(f"{i}", end=" ")

# Ejercicio 5

try:

    num=float(input("Introduzca un número: "))

    for i in range(1,11):
        print(f"{i} x {num} = {i*num}")
except ValueError:
    print("Introduzca correctamente el número.")



# Ejercicio 6 // Está mal, necesito realizarlo como en el ejercicio 7. Sería interesante usar el while true

import random
numero_aleatorio = random.randint(1, 10)  # Generamos un número aleatorio para adivinar

try:
    for i in range(1,11):
        intento=int(input("Adivina un número del 1 al 10: "))
        if intento == i :
            print("Has acertado!")
            break
        else:
            print(f"El número correcto era {i}")
            break
except ValueError:
    print("Introduzca correctamente el número")

# Ejercicio 7

import random

VIDAS = 5
numero_aleatorio = random.randint(1, 10)  # Generamos un número aleatorio para adivinar

try:
    while VIDAS > 0:
        intento = int(input(f"Adivina un número del 1 al 10, solo dispone de {VIDAS} vidas: "))
        
        if intento == numero_aleatorio:
            print("Enhorabuena, has acertado!")
            break
        else:
            VIDAS -= 1
            print("No has acertado!")
        
        if VIDAS == 0:
            print(f"Se ha quedado sin vidas,el número era  {numero_aleatorio}")
except ValueError:
    print("Por favor, ingresa un número válido.")


            

            

        
    
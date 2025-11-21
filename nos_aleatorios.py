"""
Ejercicio:
Escribe un programa en Python que genere 1000 números aleatorios. Cada números debe ser 0 o 1.
El programa nos tiene que decir cuántas veces aparece el número 0 y cúantas el nº1.
N_veces=1000
Muestra  el resultado al final del programa indicando:
    Número de veces que ha salido el cero
    Número de veces que ha salido el uno

"""

import random

# Nº de tiradas, es una constante

N_VECES=1000

# Inicializamos los contadores para luego imprimir el nº de veces
uno = 0
cero = 0


for _ in range(N_VECES):
    numero=random.randint(0, 1) # El número aleatorio tiene que estar dentro del bucle 
    if numero == 1:
        uno += 1
    elif numero == 0:
        cero += 1

print(f"el numero de veces que sale 1 : {uno*0.100:.2f}%")
print(f"el numero de veces que sale 0 : {cero*0.100:.2f}%")
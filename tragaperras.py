import random
import time
#libreria time
'''

Título: Simulación de una Máquina Tragaperras en Python



Objetivo:



Desarrolla un programa en Python que simule una máquina tragaperras de casino. El juego permitirá al usuario apostar una cantidad de dinero virtual, jugar una ronda y verificar si ha ganado o perdido. El objetivo es practicar el uso de funciones, bucles, condicionales y la manipulación de listas en Python, además de mejorar la interacción con el usuario a través de una interfaz de consola atractiva.



Descripción:



Escribe un programa que cumpla con los siguientes requisitos:



Lista de Símbolos:



Define una lista con tres símbolos diferentes (por ejemplo, frutas como '🍒', '🍋', '🍓').

Saldo Inicial:



Establece un saldo inicial de 100 unidades para el jugador.



Funciones Necesarias:



mezclar_lista(lista): Mezcla la lista de símbolos de forma aleatoria. 👌

verificar_ganador(lista): Verifica si todos los elementos de la lista son iguales, lo que indica que el jugador ha ganado.👌

limpiar_pantalla(): Limpia la consola para mejorar la presentación visual del juego.

realizar_apuesta(): Permite al jugador ingresar una apuesta válida, asegurándose de que no exceda su saldo disponible.👌

actualizar_saldo(apuesta, ganador): Actualiza el saldo del jugador según el resultado de la ronda. 👌

mostrar_menu(): Muestra un menú principal centrado con opciones para jugar, ver el saldo o salir del juego. 👌

simular_tragaperras(): Simula el efecto visual de una máquina tragaperras girando, mostrando varios estados intermedios antes de revelar el resultado final.



Bucle Principal:



Implementa un bucle principal que permita al jugador seleccionar entre jugar una ronda, ver su saldo actual o salir del juego.

Si el jugador selecciona jugar, se realiza una apuesta, se simula la máquina tragaperras y se verifica si ha ganado.

Si el jugador selecciona ver saldo, se muestra el saldo actual.

Si el jugador selecciona salir, el programa finaliza.



Validaciones:



Asegúrate de que el jugador no pueda apostar más dinero del que tiene disponible.

Si el saldo del jugador es 0, no se le permite realizar más apuestas.



Interfaz Visual:



El menú debe estar centrado y tener un marco exterior para mejorar la presentación.

La simulación de la máquina tragaperras debe mostrar varios estados intermedios para crear un efecto visual de giro.



Entregael siguiente material:



Un archivo Python (.py) con el código del juego.

Comentarios en el código explicando cada función y su propósito.



Evaluación:



Funcionalidad del programa (30%)

Uso correcto de funciones y estructuras de control (30%)

Claridad y organización del código (20%)

Manejo de errores y validaciones (20%)

Presentación visual y experiencia de usuario (10%)







'''



def mostrar_menu():
    print("""
\033[1;33m    ╔═════════════════════╗
    ║      🎰 MENÚ 🎰     ║
    ╠═════════════════════╣
    ║  1️⃣  \033[1;32mJUGAR\033[1;33m           ║
    ║  2️⃣  \033[1;34mVER SALDO\033[1;33m       ║
    ║  3️⃣  \033[1;31mSALIR\033[1;33m           ║
    ╚═════════════════════╝\033[0m
    """)

# Mostrar el saldo actual del jugador
def salario(fichas):
    """Muestra el saldo actual del jugador."""
    print(f"💰 Saldo actual: {fichas}€")


def visualizacion(array1):
    
    print(f"{' | '.join(array1[0:3])} ")
    

def mezclar_lista(array1): 
    """Devuelve 3 frutas aleatorias simulando los rodillos."""
    return random.choices(array1, k=3)
    

def realizar_apuesta(apuesta,saldo): # Como la variable apuesta y salvo van a ser modificadas, las tengo que poner aquí, entre los parentesis
    if apuesta <= 0: # Si el saldo es 0 ya no deja apostar. solo es para comprobar la apuesta no actualizar.
        print("¡No te queda más saldo!")
        
    
    while True: #Siempre y cuando haya saldo, saltara al bucle , en el caso contrario, no entra en el bucle y no pasa del primer if
        try:
            apuesta = int(input("¿Cuántas fichas desea jugar?: \n "))
            if apuesta <= 0:
                print("Debe ingresar una cantidad positiva.")
                continue

            if apuesta > saldo: # De esta manera nos aseguramos que nunca gastaremos más de lo que tenemos
                print(f"No puedes apostar más de lo que tienes. Saldo disponible: {saldo}")
            else:
                saldo -= apuesta
                print(f"Apuesta aceptada.")
                return saldo  # Retornamos el saldo actualizado
        
        except ValueError: # mirar si hay algun excep mejor
            print("Ingrese un número válido.")



def verificar_ganador(frutas_final):
    """Verifica si hay combinación ganadora y actualiza el saldo."""
    if frutas_final[0] == frutas_final[1] == frutas_final[2]:  # Si las tres frutas son iguales
        print("🎉 Enhorabuena, ¡Has ganado! 🎉")
        ganador = True
        return ganador
    else:
        print("😢 No has ganado esta vez.")
        ganador = False
        return ganador     # Devuelve el saldo actualizado (a traves del return, el programa recordara el resultado)

# Actualizar el saldo después de una ronda
def actualizar_saldo(saldo, apuesta, ganador):
    """Actualiza el saldo del jugador según el resultado de la ronda."""
    if ganador:
        saldo += apuesta  # Si ganó, se le devuelve la apuesta y se agrega el premio
        print(f"🎉 ¡Has ganado! Tu saldo ha aumentado a {saldo}€")
    else:
        saldo -= apuesta  # Si perdió, se le resta la apuesta
        print(f"😢 Has perdido. Tu saldo ha disminuido a {saldo}€")
    return saldo  # Devuelve el saldo actualizado
    

def simular_tragaperras(array1):
    """Simula el giro de la tragaperras y devuelve el resultado final."""
    print("🎰 Girando... 🎰\n")

    for _ in range(10):  # Simulamos el movimiento de los rodillos
        frutas_temporales = mezclar_lista(array1)  # 🔹 Genera nueva combinación en cada giro
        print(f"\r{' | '.join(frutas_temporales)}", end="", flush=True)  # 🔹 Sobrescribe la línea anterior
        time.sleep(0.2)  # 🔹 Pausa breve para el efecto

    # 🔹 Muestra el resultado final
    frutas_final = mezclar_lista(array1)
    print(f"\r{' | '.join(frutas_final)} ")  
    return frutas_final  # 🔹 Devuelve el resultado para usarlo en otras funciones
def salir_juego():
    print("Ha seleccionado salir del juego.")
    exit()
saldo=100
apuesta=5
frutas = ["🍒", "🍋", "🍊", "🍉", "🍇"]
azarfrutas=random.choice(frutas)
posiciones=[0,1,2]

while True:
    if saldo>0:
        mostrar_menu()
        opcion=int(input("¿Qué opción desea realizar?: \n"))

        match opcion:

            case 1: 

                visualizacion(frutas) #saldo (solo una vez al comienzo o solo printear una vez?)
                saldo = realizar_apuesta(apuesta,saldo)
                azarfrutas = mezclar_lista(frutas) 
                frutas_final = simular_tragaperras(azarfrutas) # Puedo invocar la función y al mismo tiempo pasar el return a la variable. Si no lo hago así, repetiría la función
                ganador = verificar_ganador(frutas_final,saldo,apuesta)

            case 2:

                saldo=actualizar_saldo(saldo, apuesta, ganador)
                salario(saldo)
                #solo ver saldo
            case 3:
                
                salir_juego()
    else:
        print("Te quedaste sin dinero")
        exit()
        #acabar juego


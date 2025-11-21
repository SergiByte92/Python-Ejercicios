import random
import time
import os

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


# Definimos un diseño de la máquina de tragaperras

def mostrar_maquina_tragaperras(resultados=None, saldo=None):
    """Muestra el diseño de la máquina con los resultados pasados (si existen)."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
    
    # Si no se proporcionan resultados, muestra espacios vacíos
    if resultados is None:
        resultados = [" ", " ", " "]
    
    # Alineamos bien los resultados dentro de la caja IMPORTANTE!! HACER SE PUEDE HACER QUE SOLO SEA VISIBLE EL SALDO CUANDO PULSE LA OPCION 2
    print(f"""
\033[1;33m
      ╔══════════════════════════╗
      ║    🎰 TRAGAPERRAS 🎰     ║
      ╠════════╦════════╦════════╣
      ║  {resultados[0]:^3}  ║  {resultados[1]:^3}  ║  {resultados[2]:^3}  ║
      ╠════════╬════════╬════════╣
      ║  {resultados[0]:^3}  ║  {resultados[1]:^3}  ║  {resultados[2]:^3}  ║
      ╠════════╬════════╬════════╣
      ║  {resultados[0]:^3}  ║  {resultados[1]:^3}  ║  {resultados[2]:^3}  ║
      ╠════════╩════════╩════════╣
      ║                          ║
      ║   \033[1;32m🎯 [1] JUGAR\033[1;33m           ║
      ║   \033[1;36m💰 [2] VER SALDO\033[1;33m       ║
      ║   \033[1;31m🚪 [3] SALIR\033[1;33m           ║
      ║                          ║
      ║   💰 Saldo: {saldo if saldo is not None else 'N/A':<6}€      ║
      ╚══════════════════════════╝
\033[0m
""")

# Mostrar el saldo actual del jugador
def salario(fichas):
    """Muestra el saldo actual del jugador."""
    print(f"💰 Saldo actual: {fichas}€")

# Simula el giro de la tragaperras y devuelve el resultado final
def simular_tragaperras(array1):
    """Simula el giro de la tragaperras y devuelve el resultado final."""
    print("🎰 Girando... 🎰\n")
    
    resultados = None
    for _ in range(10):  # Simulamos el movimiento de los rodillos
        frutas_temporales = random.choices(array1, k=3)  # Genera nueva combinación en cada giro
        mostrar_maquina_tragaperras(frutas_temporales)  # Actualiza la pantalla de la máquina
        time.sleep(0.2)  # Pausa breve para el efecto

    # Muestra el resultado final
    resultados = random.choices(array1, k=3)
    mostrar_maquina_tragaperras(resultados)  # Muestra la combinación final
    return resultados  # Devuelve el resultado para usarlo en otras funciones

# Lista de frutas o símbolos para la tragaperras
frutas = ['🍒', '🍋', '🍉', '🍇', '🍊', '🍎']

def realizar_apuesta(saldo):
    """Permite al jugador realizar una apuesta."""
    while True: 
        try:
            apuesta = int(input("¿Cuántas fichas desea jugar?: \n"))
            if apuesta <= 0:
                print("Debe ingresar una cantidad positiva.")
                continue

            if apuesta > saldo:  # Asegura que no apueste más de lo que tiene
                print(f"No puedes apostar más de lo que tienes. Saldo disponible: {saldo}")
            else:
                saldo -= apuesta
                print(f"Apuesta aceptada.")
                return saldo, apuesta  # Retorna saldo actualizado y la apuesta realizada

        except ValueError:
            print("Ingrese un número válido.")

def verificar_ganador(frutas_final):
    
    if frutas_final[0]=="🍒" and frutas_final[1]=="🍒" and frutas_final[2]=="🍒":  # solo son 3 cerezas el premio gordo #Asignar premios? en vez de true devolver premio/premio gordo
        print("🎉 Enhorabuena, ¡Has ganado! 🎉")
        return True  # El jugador ganó
    else:
        print("😢 No has ganado esta vez.")
        return False  # El jugador perdió

def actualizar_saldo(saldo, apuesta, ganador):

    """Actualiza el saldo del jugador según el resultado de la ronda."""
    if ganador:
        saldo += apuesta * 2  # Si ganó, se le devuelve la apuesta + premio
        print(f"🎉 ¡Has ganado! Tu saldo ha aumentado a {saldo}€")
    else:
        
        print(f"😢 Has perdido. Tu saldo ha disminuido a {saldo}€")
    return saldo  # Devuelve el saldo actualizado

def salir_juego():

    print("Ha seleccionado salir del juego.")
    exit()

# Configuración inicial
saldo = 100
frutas = ["🍒", "🍋", "🍊", "🍉", "🍇"]

while True:
    if saldo > 0:
        mostrar_maquina_tragaperras(frutas,saldo)
        opcion = int(input("¿Qué opción desea realizar?: \n"))

        match opcion:
            case 1:  # Jugar
                saldo, apuesta = realizar_apuesta(saldo)
                frutas_final = simular_tragaperras(frutas)
                ganador = verificar_ganador(frutas_final)
                saldo = actualizar_saldo(saldo, apuesta, ganador)

            case 2:  # Ver saldo
                salario(saldo) # Printear el mismo diseño pero donde salen las frutas que aparezca el saldo?

            case 3:  # Salir
                salir_juego()

    else:
        print("Te quedaste sin dinero. Fin del juego.")
        exit()
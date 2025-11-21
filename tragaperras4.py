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

def mostrar_maquina_tragaperras(resultados, resultados2, resultados3, saldo=None, mensaje=None):
    """Muestra el diseño de la máquina con los resultados y un mensaje opcional."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Asegurar que los resultados sean listas de 3 elementos
    resultados = resultados if resultados else [" ", " ", " "]
    resultados2 = resultados2 if resultados2 else [" ", " ", " "]
    resultados3 = resultados3 if resultados3 else [" ", " ", " "]
    
    # Formatear el mensaje
    mensaje_display = mensaje if mensaje else ""
    saldo_display = saldo if saldo is not None else 'N/A'
    
    print(f"""
\033[1;33m
      ╔══════════════════════════╗
      ║    🎰 TRAGAPERRAS 🎰     ║
      ╠════════╦════════╦════════╣
      ║  {resultados[0]:^3}  ║  {resultados[1]:^3}  ║  {resultados[2]:^3}  ║
      ║        ║        ║        ║
      ║  {resultados2[0]:^3}  ║  {resultados2[1]:^3}  ║  {resultados2[2]:^3}  ║
      ║        ║        ║        ║
      ║  {resultados3[0]:^3}  ║  {resultados3[1]:^3}  ║  {resultados3[2]:^3}  ║
      ╠════════╩════════╩════════╣
      ║                          ║
      ║   \033[1;32m🎯 [1] JUGAR\033[1;33m           ║
      ║   \033[1;36m💰 [2] VER SALDO\033[1;33m       ║
      ║   \033[1;31m🚪 [3] SALIR\033[1;33m           ║
      ║                          ║
      ║                          ║
      ║ {mensaje_display:<17}        ║
      ╚══════════════════════════╝
\033[0m
""")

# Mostrar el saldo actual del jugador
def salario(fichas):
    """Muestra el saldo actual del jugador."""
    print(f"💰 Saldo actual: {fichas}€")

def simular_tragaperras(frutas, resultados, resultados2, resultados3):
    """Simula un giro vertical donde los símbolos caen de arriba hacia abajo."""
    print("🎰 Girando... 🎰\n")

    for _ in range(10):
        # Generar una nueva fila superior
        nueva_fila = random.choices(frutas, k=3)

        # Simular el desplazamiento hacia abajo
        resultados3 = resultados2  # Lo del medio va abajo
        resultados2 = resultados   # Lo de arriba va al medio
        resultados = nueva_fila   # Lo nuevo entra arriba

        # Mostrar esta transición
        mostrar_maquina_tragaperras(resultados, resultados2, resultados3)
        time.sleep(0.2)

    return resultados, resultados2, resultados3



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

def verificar_ganador(resultados, resultados2, resultados3):
    # Premio gordo (todas las cerezas en una línea horizontal)
    if resultados2[0] == "🍒" and resultados2[1] == "🍒" and resultados2[2] == "🍒" :
       
        return "Premio Gordo", "🎉 ¡Premio Gordo! 🎉"
    
    # Premio diagonal (de esquina a esquina)
    if  resultados[0] == resultados2[1] ==  resultados3[2]  or \
        resultados[2] == resultados2[1] == resultados3[0] :
        return "Premio Diagonal", "🎉 ¡Premio Diagonal! 🎉"
    
    # Premio vertical (misma columna en las tres filas)
    for i in range(3):
        if resultados[i] ==  resultados2[i] ==  resultados3[i] :
            return "Premio Vertical", "🎉 ¡Premio Vertical! 🎉"
    
    # Premio horizontal (misma fila en las tres columnas)
    for i in range(3):
        if resultados[0] ==  resultados[1] ==  resultados[2] or \
           resultados2[0] ==  resultados2[1] ==  resultados2[2] or\
           resultados3[0] ==  resultados3[1] ==  resultados3[2]:
            return "Premio Horizontal", "🎉 ¡Premio horizontal! 🎉"
    
    # Si no hay ganador
    return False, "😢 No has ganado esta vez."

def actualizar_saldo(saldo, apuesta, ganador):
    """Actualiza el saldo del jugador según el resultado de la ronda."""
    if ganador:
        # Diferentes premios podrían tener diferentes multiplicadores
        if ganador == "Premio Gordo":
            multiplicador = 5
        else:
            multiplicador = 2
        
        ganancia = apuesta * multiplicador
        saldo += ganancia
        mensaje = f"¡Has ganado {ganancia}€!"
    else:
        saldo -= apuesta
        mensaje = f"Has perdido {apuesta}€."
    
    return saldo, mensaje

def salir_juego():

    print("Ha seleccionado salir del juego.")
    exit()

# Configuración inicial
saldo = 100
frutas = ["🍒", "🍋", "🍑", "🍉", "🍇"]
mensaje = None

# Inicializamos las tres filas con combinaciones aleatorias
resultados = random.choices(frutas, k=3)
resultados2 = random.choices(frutas, k=3)
resultados3 = random.choices(frutas, k=3)

# Bucle principal corregido
while True:
    if saldo > 0:
        # En tu bucle principal:
        mostrar_maquina_tragaperras(resultados, resultados2, resultados3, saldo, mensaje)

        while True:
            try:
                opcion = int(input("¿Qué opción desea realizar?: \n"))
            except ValueError:
                print("Por favor,introduzca alguna de las opciones del menu")
                continue
                


            match opcion:
                case 1:  # Jugar
                    saldo, apuesta = realizar_apuesta(saldo)
                    resultados, resultados2, resultados3 = simular_tragaperras(frutas, resultados, resultados2, resultados3)
                    ganador, mensaje = verificar_ganador(resultados, resultados2, resultados3)
                    saldo,mensaje = actualizar_saldo(saldo, apuesta, ganador)
                    mostrar_maquina_tragaperras(resultados, resultados2, resultados3, saldo, mensaje)
                    input("Presiona Enter para continuar...")

                case 2:  # Ver saldo
                    mostrar_maquina_tragaperras(resultados, resultados2, resultados3, saldo, f"Saldo actual:{saldo}€")
                    input("Presiona Enter para continuar...")

                case 3:  # Salir
                    salir_juego()
    else:
        print("Te quedaste sin dinero. Fin del juego.")
        exit()
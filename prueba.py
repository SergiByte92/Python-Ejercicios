import os
import random

def mostrar_maquina_tragaperras(resultados, resultados2, resultados3, saldo=None, mensaje_premio=None):
    """Muestra el diseño de la máquina con los resultados pasados (si existen)."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
    
    # Si no se proporcionan resultados, muestra espacios vacíos
    if resultados is None:
        resultados = [" ", " ", " "]
    if resultados2 is None:
        resultados2 = [" ", " ", " "]
    if resultados3 is None:
        resultados3 = [" ", " ", " "]
    
    # Mensaje de premio si lo hay
    premio_mensaje = f"🎉 ¡Has ganado! {mensaje_premio}" if mensaje_premio else "🎰 ¡SIGA JUGANDO!"
    
    # Mostrar la máquina de tragaperras con los resultados y el saldo
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
      ║   \033[1;32m🎯 [1] JUGAR \033[1;33m   \033[1;36m💰 [2] VER SALDO \033[1;33m  \033[1;31m🚪 [3] SALIR\033[1;33m  ║
      ║                          ║
      ║   {premio_mensaje:<26}  ║
      ║                          ║
      ║   💰 Saldo: {saldo if saldo is not None else 'N/A':<6}€      ║   
      ╚══════════════════════════╝
\033[0m
""")
    
# Configuración inicial
saldo = 100
frutas = ["🍒", "🍋", "🍊", "🍉", "🍇"]

# Inicializamos las tres filas con combinaciones aleatorias
resultados = random.choices(frutas, k=3)
resultados2 = random.choices(frutas, k=3)
resultados3 = random.choices(frutas, k=3)


mostrar_maquina_tragaperras(resultados,resultados2,resultados3,saldo)

# Mostrar el saldo actual del jugador
def salario(fichas):
    """Muestra el saldo actual del jugador."""
    print(f"💰 Saldo actual: {fichas}€")

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

# Ejemplo de uso
saldo = 50  # Saldo inicial
apuesta = 10  # Monto de la apuesta
ganador = True  # Aquí sería el resultado de la ronda (True si gana, False si pierde)

# Mostrar el saldo inicial
salario(saldo)

# Actualizar el saldo después de la ronda
saldo = actualizar_saldo(saldo, apuesta, ganador)

# Mostrar el saldo final
salario(saldo)

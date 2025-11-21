import os
import random
import time

def mostrar_maquina_tragaperras(resultados=None):
    """Muestra un diseño mejorado de máquina tragaperras con colores y estilo."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
    
    if resultados is None:
        resultados = ["❓", "❓", "❓"]
    
    # Definimos colores para diferentes símbolos (usando emojis)
    colores = {
        "🍒": "\033[1;31m",  # Rojo
        "🍋": "\033[1;33m",  # Amarillo
        "🍉": "\033[1;32m",  # Verde
        "🍇": "\033[1;35m",  # Morado
        "🍊": "\033[1;38;5;208m",  # Naranja
        "🍎": "\033[1;91m",  # Rojo claro
        "❓": "\033[1;37m",  # Blanco
        "7": "\033[1;31m",   # Rojo (símbolo clásico)
        "★": "\033[1;33m"    # Amarillo (estrella)
    }
    
    # Aplicamos colores a los resultados
    simbolos_coloreados = []
    for simbolo in resultados:
        color = colores.get(str(simbolo), "\033[1;37m")  # Blanco por defecto
        simbolos_coloreados.append(f"{color}{simbolo}\033[0m")
    
    # Diseño mejorado con más elementos visuales
    print(f"""
    \033[1;36m╔══════════════════════════════════╗
    ║  🎰 \033[1;37mTRAGAPERRAS VIRTUAL\033[1;37m 🎰     ║
    ╠════════════╦══════════╦════════════╣
    ║            ║          ║            ║
    ║    {simbolos_coloreados[0]:^2}      ║    {simbolos_coloreados[1]:^2}    ║     {simbolos_coloreados[2]:^2}     ║
    ║            ║          ║            ║
    ╠════════════╩══════════╩════════════╣
    ║                                    ║
    ║   \033[1;32m►► JUGAR \033[1;36m│ \033[1;31mSALIR ■\033[1;36m ◄◄   ║
    ╚══════════════════════════════════╝\033[0m
    """)

def simular_tragaperras(array_symbols, delay=0.2, spins=10):
    """Simula el giro de la tragaperras con animación."""
    print("\n🎰 ¡Girando los rodillos! 🎰\n")
    time.sleep(1)
    
    resultados = None
    for _ in range(spins):
        # Genera una combinación temporal con posible animación
        temp_results = random.choices(array_symbols, k=3)
        
        # Efecto visual: a veces muestra parcialmente el resultado final
        if _ > spins - 3 and random.random() > 0.5:
            temp_results = [random.choice([r, random.choice(array_symbols)]) 
                          for r in (resultados if resultados else temp_results)]
        
        mostrar_maquina_tragaperras(temp_results)
        time.sleep(delay * (1 + _/spins))  # Aumenta el delay progresivamente
    
    # Resultado final
    resultados = random.choices(array_symbols, k=3)
    mostrar_maquina_tragaperras(resultados)
    
    # Efecto especial para combinaciones ganadoras
    if len(set(resultados)) == 1:  # Si todos son iguales
        print("\n\033[1;33m✨ ¡FELICIDADES! ¡GANASTE! ✨\033[0m\n")
    elif resultados[0] == resultados[1] or resultados[1] == resultados[2]:
        print("\n\033[1;32m🎉 ¡Casi! ¡Inténtalo de nuevo! 🎉\033[0m\n")
    
    return resultados

# Símbolos para la tragaperras (emojis y símbolos clásicos)
simbolos = ['🍒', '🍋', '🍉', '🍇', '🍊', '🍎', '7', '★']

# Ejecutamos la simulación
if __name__ == "__main__":
    while True:
        resultado = simular_tragaperras(simbolos)
        
        # Opción para continuar o salir
        opcion = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if opcion != 's':
            print("\n\033[1;35m¡Gracias por jugar! ¡Vuelve pronto!\033[0m\n")
            break
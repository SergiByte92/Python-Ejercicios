valor= input("introduce un numero: ")
# Multiplica por 3

valor = valor *3 
print(valor)

valor *= 3 # Es lo mismo de arriba, pero como el valor ha cambiado tras la primera operacion, cambia el resultado y son 9 digitos(3*3)
print(valor)

# Dividir entre 5
# Valor = valor / 5
valor = 13
valor  /= 5
print(valor)

# Division entera // 

valor = 13
valor //= 5
print(valor)

# Módulo %

valor =7
resultado = valor %3
print(f"El resto de dividir {valor} entre 3 es {resultado}")

numero=int(input("introduce un numero: "))
numero **=3
print(f"elevado al cubo: {numero}")
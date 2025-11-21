# Suma los números del 25 al 0 (inclusive), en orden descendente
# Resultado: La suma del 25 al 0 es: 325


# Inicializamos la suma en 0
suma = 0

# Recorremos los números del 25 al 0
for i in range(25, -1, -1): # -1 el end ya que quiero que acabe en el 0 y paso -1 porque quiero que sea descendente
    suma += i

# Mostramos el resultado
print(f"La suma del 25 al 0 es : {suma}")


# Otra manera de hacerlo 

# Usamos la función sum() junto con range para obtener la suma de los números del 25 al 0
resultado = sum(range(0, 26))

# Mostramos el resultado
print(f"La suma del 25 al 0 es : {resultado}")


""" edad= int(input("introduce tu edad: "))
es_adulto = "si" if edad >=18 else "No" # Operador TERNARIO
print(f"Eres adulto? {es_adulto}")

# otro ejemplo
a, b = 10, 20
mayor = a if a > b else b # Operador ternario
print(f" el mayor de {a} y {b} es {mayor}")
 """
# Pedir al usuario un numero y utilizando el operador ternario me dia si es par o impar
""" try:
    num= int(input("Introduce un numero: "))
    es_par= "es par"if num%2== 0  else "es impar"
    print(f"El numero introducido {num} {es_par}")
except ValueError:
    print("❌ ERROR, Introduce un numero")
 """
# OPERADOR TERNARIO ANIDADO (A evitar)

edad = 17
mensaje = "Niño" if edad < 12 else "Adolescente" if edad <18 else "Adulto"
print(f"{mensaje}")


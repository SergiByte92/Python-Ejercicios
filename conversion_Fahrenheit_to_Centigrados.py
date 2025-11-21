# Pedir al usuario una temperatura en ºF y convertirla en ºC
# Deberas utilizar caracteres unicode para el simbolo del grado
# Resultado con 2 decimales
# Utilizar el try
try:
    fahrenheit=float(input("Introduzca la temperatura en \u00b0F: "))
    celsius=(fahrenheit-32)*(5/9)

    print(f"La temperatura {fahrenheit:.2f}\u00b0F en grados centrigrados es : {celsius:.2f}\u00b0C.")
except ValueError:
    print("❌ ERROR. Introduzca correctamente la temperatura.")


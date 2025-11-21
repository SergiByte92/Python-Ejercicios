# Convertir cadenas a números

no_cadena= '10'
#print(f"Le sumo una unidad a {no_cadena} = {no_cadena+1}") # Error de sintaxis
print(f"Le sumo una unidad a {no_cadena} = {no_cadena}+1")  # Estoy concatenando


no_cadena= int(no_cadena)

print(f"Le sumo una unidad a {no_cadena} = {no_cadena}+5")  # Pinta 10+5
print(f"Le sumo una unidad a {no_cadena} = {no_cadena+5}")  # Realiza la suma aritmética

# Pedir al usuario un numero y que me devuelva el doble de ese número

numero=float(input("introduce un número: ")) # int -> convierte a nº entero, float -> convierte a nº CON  DECIMALES

print(f"El doble de {numero:.0f} es : {numero*2:.2f}") 
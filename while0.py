# Ejercicio: Contar el número total de dígitos que tiene un número

# Por ejemplo, el número 75893, tenría 5 dígitos
""""
original = num = 847
count = 0
while num !=0:
    num = num // 10 # La división entera se queda con la parte entera
    count = count + 1

print (f"El número {original} tiene {count} dígitos")

"""
try:
    original = num = int(input("Introduzca un número: "))
    count = 0
    while num !=0 and num.isdigit():
        num = num // 10 # La división entera se queda con la parte entera
        count += 1

    print (f"El número {original} tiene {count} dígitos")


except ValueError:
    print("❌ ¡ERROR!. Introduzca correctamente el número")




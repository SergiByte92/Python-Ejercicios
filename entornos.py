# Definimos la tabla de letras
array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']

# Solicitar al usuario el número y la letra
numero = input("Introduce un número de 8 dígitos: ")
letra = input("Introduce una letra: ").upper()

# Verificar que el número tenga exactamente 8 dígitos
if len(numero) != 8 or not numero.isdigit():
    print("Número incorrecto. Debe tener 8 dígitos.")
else:
    # Convertimos el número a entero
    num = int(numero)

    # Calcular el resto
    resto = num % 23

    # Obtener la letra según la posición del resto en el array
    letraf = array[resto]

    # Comparar la letra ingresada con la letra obtenida
    if letra == letraf:
        print("Es correcto.")
    else:
        print("Es incorrecto.")

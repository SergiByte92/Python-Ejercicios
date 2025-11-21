
# Nuestro PIN secreto 2935

pin_secreto="2935"

# Bucle anidado para probar todas las combinaciones posibles de 4 dígitos

for d1 in range(10): # Primer dígito (0-9)
    for d2 in range(10): # Segundo dígito(0-9)
        for d3 in range(10): # Tercero dígito(0-9)
            for d4 in range(10): # Cuarto dígito(0-9)
                intento=f"{d1}{d2}{d3}{d4}"
                print(f"Probando PIN: {intento}")
                if intento == pin_secreto:
                    print(f"¡ 👍 PIN encontrado! El PIN es {intento}")
                    break # sal del bucle interno
            if intento == pin_secreto: # sal del bucle, si no lo uso, el bucle sigue activo.
                break
        if intento == pin_secreto: # sal del bucle
            break
    if intento == pin_secreto: # sal del bucle
        break
        


"""

# Nuestro PIN secreto
pin_secreto ="2935"

# Bucle anidado para probar todas las combinaciones posibles de 4 dígitos
for d1 in range(10):  # Primer dígito (0-9)
    for d2 in range(10):  # Segundo dígito (0-9)
        for d3 in range(10):  # Tercer dígito (0-9)
            for d4 in range(10):  # Cuarto dígito (0-9)
                intento = f"{d1}{d2}{d3}{d4}"
               
                if intento == pin_secreto:
                    print(f"¡PIN correcto encontrado!{intento}" )
                    break

"""

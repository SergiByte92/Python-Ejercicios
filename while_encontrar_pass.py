# Dada una contraseña, adivinarla en un número maximo de intentos
password_secreto="admin123"

# Límite de intentos máximo

MAX = 5
intentos = 0 
acceso_concedido = False # True o False siempre en mayuscula

while intentos < MAX: # Cinco intentos, si intentos = 1 entonces sería  <=5
    intento=input("Introduce la contraseña: ")
    intentos +=1
    if intento == password_secreto:
        print("❤️ Acceso concedido")
        acceso_concedido=True
        break

    else:
        print(f"❌ Contraseña incorrecta. Intento {intentos} de {MAX}")

if not acceso_concedido: 
    print("Se han agotado todos los intentos. El sistema se ha bloqueado")




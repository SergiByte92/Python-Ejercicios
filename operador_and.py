# Operador lógico AND (Y)

# El operador lógico AND devuelve un True si ambos valores a evaluar son verdaderos

condicion1 = False
condicion2 = False

resultado = condicion1 and condicion2
#print(f"El resultado de {condicion1} y {condicion2} = {resultado}")

# Ejercicio: Pedir al usuario un numero entre 10 y 50

# Pedimos un numero 
#numero = int(input("Introduce un numero entre 10 y 50: "))

# Verificar si este numero esta dentro del rango

#if numero >= 10 and numero <= 50 :
#    print("💕 esta dentro, tontorron")    # otra manera : dentro de las comillas Windows y punto a la vez 
#else:
#    print("Eres un cafre 🤢")

# Ejercicio: Pedir usuario y contraseña y comparala con :
# usuario=admin
# password = 1234

usuario ="admin"
password = "1234" #si no pongo comillas es un integer

usuario2=(input("Introduze el usuario : "))

password2=(input("Introduzca la contraseña"))

if usuario2 == usuario and password == password2:
    print("Estas dentro crack")
else:
    print("Haber estudiado,ERROR! 🤢")
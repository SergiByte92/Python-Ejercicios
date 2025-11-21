# Pedir la edad al usuario, si la edad menor que 0. Saldra diciendo que la edad no puede ser negativa
#Si edad es menor o igual a 12. Nos dira que eres un niño
#Si edad es menor o igual a 17. Nos dira que eres un adolescente
#Si edad es menor o igual a 30 eres un jove adulto
#Si edad es menor o igual a 64. Nos dira que eres un adulto
#En caso contrario, todavia estas vivo????
try:

    edad=int(input("Introduzca tu edad: "))

    if (edad<0):
        print("❌ ERROR: La edad no puede ser negativa")
    elif(edad<=12):
        print("Eres un niño 👍")
    elif(edad<=17):
        print("Eres un adolescente 😁")
    elif(edad<=30):
        print("Eres un jove adolescente 👌")
    elif(edad<=64):
        print("Eres un adulto 😍")
    else:
        print("Todavia estas vivo????? 😱")

except ValueError: 
    print("❌ ERROR. Debes de introducir un numero valido")


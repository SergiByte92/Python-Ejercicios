# Pedir al usuario un número entero y el programa nos diga si este número es divisible por 2 y por 3
try:
    num=int(input("Introduzca un número: "))

    mod2=num%2 #Podría haberlo hecho directamente desde la variable num
    mod3=num%3

    if mod2 == 0 and mod3==0:
        print(f"El {num} es divisible entre 2 y 3")

    elif mod2 == 0 and mod3!=0:
        print("Es divisible entre 2 pero no entre 3")
    
    elif mod2!=0 and mod3==0:
        print("Es divisible entre 3 pero no entre 2")
    
    elif mod2!=0 and mod3!=0:
        print("No es divisible entre ningun número")

except ValueError :
    print("❌ ERROR . Introduzca correctamente el número.")
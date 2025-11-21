try:

    codigo= int(input("Introduce un código: "))

    match codigo:
        case 200:
            print ("El código 200, es todo correcto")
        case 301:
            print ("El código 301, la página ha sido movido de lugar")
        case 302:
            print ("El código 302, la página se ha movido temporalmente")
        case _:
            print("Código no reconocido") # El caracter _ hace de comodín,esta opción se da cuando no se produce ninguno de los casos anteriores

except ValueError:
    print("❌ ERROR. Introduzca correctamente el código")
   

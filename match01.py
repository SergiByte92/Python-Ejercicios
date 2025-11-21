
def weekday(n): # n será un nº que corresponderá con el día de la semana
   
    match n:
        case 1: return "Lunes"
        case 2: return "Martes"
        case 3: return "Miercoles"
        case 4: return "Jueves"
        case 5: return "Viernes"
        case 6: return "Sabado"
        case 7: return "Domingo"
        case _: return "Número de día de la semana es invalido"

while True:                   #Bucle infinito
    try:
        n=int(input("introduzca un numero del 1 al 7 : "))
        print (weekday(n))
    except ValueError:
        print("❌ ERROR. Introduzca correctamente el día de la semana.")





    
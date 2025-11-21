# Realizar un programa que pida una nota [0, 10]
# si nota <5 Suspendido
# Si nota mayor o igual a 5 y inferior a 7 bien
# Si nota igual o mayor a 7 e inferior 9. Notable
# Si nota mayor a 9 e infeiror a 10 Excelente
# Si nota es un diez. Matricula de honor
# En cualquier otro caso : Nota fuera de rango

# Se pide utilizar la instrucción match




try:
    nota=float(input("Introduzca su nota: ")) # Por otra parte, el usuario puede introducir una nota con decimales, pero siempre se redondea en números enteros.

    match nota:
        case _ if 0<=nota<5:
            print(" Suspendido. Estudia más!🫵")
        case _ if 5<=nota<7:
            print(" Bien. Progesas adecuadamente 👍")
        case _ if 7<=nota<9:
            print(" Notable. Sigue así!✌️")
        case _ if 9<=nota<10:
            print(" Excelente. Estas en el camino a la perfección!🤙")  # Al usuario se le ha olvidado incluir el caso en el que la nota sea un 9
        case _ if nota==10:
            print(" Matricula de honor. GOAT!🐐")
        case _:
            print("Nota fuera de rango!")
except ValueError:
    print("❌ ERROR! . Introduzca correctamente la nota!")

    
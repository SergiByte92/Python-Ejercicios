# Pedir al usuario que introduzca las notas de los diferentes módulos [0,10] El programa tiene que calcular y mostrar la media de las notas introducidas con dos decimales. Me dirá tambien si he aprobado.

# Crar el array calificaciones



calificaciones = []

notas = int(input("¿Cuántas notas desea introducir?: "))

for _ in range(notas):
    while True:  # Si quiero que se cumpla una condición, es interesante usar el While True, también podria haber usado el NONE
        try:
            nota = float(input("Introduzca una nota del 0 al 10: "))
            if 0 <= nota <= 10:
                calificaciones.append(nota)
                break  # Sale del while si la nota es válida
            else:
                print("Error: La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Error: Introduzca un número válido.")

numero_notas = len(calificaciones)
if numero_notas > 0:
    print(f"La nota media es {sum(calificaciones) / numero_notas:.2f}")
else:
    print("No se introdujeron notas válidas.")


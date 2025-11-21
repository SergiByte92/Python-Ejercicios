import datetime #de aquí saco fecha y hora actual
import random #nº aleatorio


# Mostrar menú
print("Menú de opciones: ")
print("\t 1️⃣- Saludar")
print("\t 2️⃣- Mostrar fecha y hora actual")
print("\t 3️⃣- Mostrar un número aleatorio")
print("\t 4️⃣- Salir")

# Pedir al usuario una opción:
opcion=int(input("Selecciona una opcion [1-4] : "))

match opcion:
    case 1:
        print("Hola que tal")
    case 2:
        ahora=datetime.datetime.now()
        # Formateo la salida
        fecha_formateada = ahora.strftime("Hoy estamos a %d/%m/%Y y son las %H:%M:%S")
        print(f"{fecha_formateada}")
    case 3:
        print(f"EL número aleatorio generado es : {random.randint(1,10)}")
    case 4:
        print("Saliendo del programa...Hasta luego")
    case _:
        print("Opción no válida")
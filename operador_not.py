# Revisar si una variable esta dentro de un rango [1,10]

dato= int(input("Introduce un numero entero [1,10]: "))
esta_dentro_rango= dato>0 and dato <11
if (dato and esta_dentro_rango):
    print(f"La variable introducida por el usuario está Dentro del rango[1,10]: {dato}")

else:
    print(f"La variable introducida por el usuario está FUERA del rango[1,10]: {dato}")
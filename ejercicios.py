cadena="python"

print(cadena[::1]) #invertimos cadena

cadena2 = "0123456789"

print(cadena2[1::2])
print(cadena2[::2])
print(cadena2[2:7:2])

cadena3="abcdefghij"
print(f"La longitud de la cadena '{cadena3}' es {len(cadena3)}")
print(f"La longitud de la cadena \"{cadena3}\" es {len(cadena3)}")

print(cadena3[:len(cadena3)//2]) #Desde el principio hasta el final, en este caso le indico que es la mitad de la cadena. // es division entera

mitad=int(len(cadena3)/2)
print(cadena3[:mitad])

print(cadena3[mitad:]) # Pintar la otra mitad

numero=input("introduzca un numero: ")

print(f"el numero introducido es  {numero} y es de tipo {type(numero)}")

invertir=numero[::-1]

print(f"la cadena invertida es : {invertir}")
resultado = " ".join(invertir)
print(resultado)
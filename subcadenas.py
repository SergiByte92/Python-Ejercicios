# Manejo de subcadenas (strings)
cadena="hola_mundo!"

# obtenemos la subcadena [inicio:fin(sin incluir)]

subcadena1=cadena[0:4]
print(f"Primera subcadena: {subcadena1}")

# Obtener una subcadena DESDE EL PRINCIPIO

subcadena2=cadena[:6] 
print(f"Segunda subcadena (desde el cero hasta el caracter 6): {subcadena2} ")

# Obtener una subcadena DESDE EL FINAL

subcadena3=cadena[5:]
print(f"Tercera subcadena (desde el caracter 5 hasta el final): {subcadena3}")

# cadena= "hola mundo!"
subcadena4=cadena[-9:-1]
print(f"Cuarta subcadena (desde el caracter -9 hasta el -1): {subcadena4}")

#EJERCICIOS

cadena2 = "abcdefg"

#Tambien se puede hacer así

print(f"{cadena2[1:3]}")
print(f"{cadena2[:5:2]}")
print(cadena2[5:])
print(cadena2[:-1])  
print(cadena2[::-1]) #Invertimos cadena

#Realizado

subcadena5=cadena2[1:3]
print(f"La subcadena 5 es : {subcadena5}")

subcadena6=cadena2[3:5]
print(f"La subcadena 6 es : {subcadena6}")

subcadena7=cadena2[0]+cadena2[2]+cadena2[4]
print(f"La subcadena 7 es : {subcadena7}")

subcadena8=cadena2[5:]
print(f"La subcadena 8 es : {subcadena8}")

subcadena9=cadena2[:-1]
print(f"La subcadena 9 es : {subcadena9}")



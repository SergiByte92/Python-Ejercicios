# buscar subcadenas

cadena="hola mundo!"

indice=cadena.find("mundo")
print(f"Indice de la cadena mundo: {indice}")
indice=cadena.find("hola")
print(f"Indice de la cadena mundo: {indice}") #Python es sensible a mayus. minusc.
#En caso de que el procedimiento .find() NO ENCUENTRE CADENA -1
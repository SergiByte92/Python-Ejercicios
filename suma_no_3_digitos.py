"""
Ejercicio: Escribe un programa que dado un número de 3 dígitos, nos de la suma de sus dígitos.
No vale utilizar ninguna función que me ayude al cálculo
Por ejemplo, si el número es 321 , la suma sería 3 +2 + 1 = 6

EJEMPLO:

% => Me quedo con el resto ( 240 % 10 el resto es 0)
/ / => Me quedo con la parte entera ( 240 // 100 la parte entera es 2 )

numero=240
digito1 = numero//100 # Centenas (División entera) 240 // 100 = 2 
digito2 = (numero//10) % 10 # Decenas (División entera) 240 //10 = 24 % 10 (porcentaje = me quedo con el resto, en este caso 4)
digito3 = numero % 10 # Unidades 240 % 10 (el resto es 0)
suma= digito1+ digito2 + digito3
print(f"La suma de  {digito1} {digito2} y {digito3} es de : {suma}")

"""
# Solicitar al usuario un número de 3 dígitos


while True:
    try:
        numero = int (input ("introduce un número de 3 dígitos: "))
        if 100 <= numero <= 999: # Verifico que sean 3 dígitos
            digito1 = numero//100
            digito2 = (numero//10) % 10
            digito3 = numero % 10
            suma = digito1 + digito2 + digito3 
            
            break
        else:
            print("Introduzca un número de 3 dígitos")


    except ValueError:
        print("❌ Error : Introduce un número valido")
    
print(f"La suma de {digito1} , {digito2} y {digito3} es de : {suma} ")
        

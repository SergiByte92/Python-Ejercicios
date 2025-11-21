# variables en python

a=3

nombre="Sergi"
edad= 22
altura=2.20

is_Profe= True
print("Te llamas", nombre)
print(f"te llamas {nombre} tienes {edad} años y mides {altura:.3f} metros y eres profe: {is_Profe}")  #f es format moderno

tresdiscos= """ 
             # 
            ###
           #####

"""
print(tresdiscos)

torres = ["tresdiscos","tresdiscos","tresdiscos"] #Array

print(torres)

"""
    1.- Las variables deben de comenzar por : "_" o una letra
    2.- El resto puede ser (a-z,A-Z.0-9)
    3.- NO se pueden utilizar palabras reservadas (for, while, print)
    4.- Python es CASE SENSITIVE (sensible a mayusculas y minusculas)

"""

x=2
resultado= (x^2) 
print("El valor del polinomio es : ")

print((x^2) + (1/2)*(x^3)+2*(x^2-x))

print(f"El valor del polinomio para x = {x} es : {resultado:.2f}")




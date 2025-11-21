# Ejercicio 2 : Imprimir los números del 1 al 20
# Para números divisibles por 3, imprimir "Fizz"
# Para números divisibles por 5, imprimir "Buzz"
# Para número divisibles por 3 y 5, imprimir "FizzBuzz"
# En cualquier otro caso, imprimir el número

for i in range (1,21):
    
    if i%3==0 and i%5==0: #Las condiciones más restrictivas al comienzo del programa.
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(f"{i}")

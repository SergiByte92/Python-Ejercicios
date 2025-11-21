# Pedir al usuario dos números y que haga de nuestro programa haga la division

try:

    num1= float(input("introduce el primer número: "))
    num2= float(input("Introduce el segundo número: "))

    resultado=num1/num2

    print(f"El número {num1} / {num2} = {resultado}")

except ZeroDivisionError:
    print("❌ ERROR No se puede realizar la division entre cero")
except ValueError:
    print("❌ ERROR Tiene que introducir un número")
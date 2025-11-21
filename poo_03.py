
# Ejercicio: Crea una clase CuentaBancaria con
# con  los siguientes ATRIBUTOS: titular, saldo
# con los siguientes Métodos: depositar(cantidad), retirar(cantidad), mostrar_saldo()
# Realizar el diagrama de clase UML

class CuentaBancaria :
    def __init__(self,titular,saldo):
        self.titular = titular # Atributo titular
        self.saldo = saldo  # Atributo saldo
    def depositar(self,cantidad):
        self.saldo += cantidad
    
    def retirar(self,cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes") # Estas intentando sacar más dinero del que tienes
    def mostrar_saldo(self):
        print(f"El titular {self.titular}, tu saldo es de : {self.saldo}")
    
luis = CuentaBancaria('Luis', 100)
luis.depositar(50)
luis.mostrar_saldo() #150
luis.retirar(149)
luis.mostrar_saldo() # 1
luis.retirar(2) # Fondos insufivientes, estas intentando sacar 2€ pero en la cuenta tienes sólo 1€
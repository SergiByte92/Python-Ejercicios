
# Ejercicio: Crea una clase CuentaBancaria con
# con  los siguientes ATRIBUTOS: titular, saldo
# con los siguientes Métodos: depositar(cantidad), retirar(cantidad), mostrar_saldo()
# Realizar el diagrama de clase UML

class CuentaBancaria :
    def __init__(self,titular,saldo):
        self.titular = titular # Atributo titular
        self.__saldo = saldo  # Atributo PRIVADO saldo -> SÓLO se peude acceder a este atributo desde DENTRO de la clase, pero NO desde fuera
    def depositar(self,cantidad):
        self.__saldo += cantidad
    
    def retirar(self,cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes") # Estas intentando sacar más dinero del que tienes
    def mostrar_saldo(self):
        print(f"El titular {self.titular}, tu saldo es de : {self.__saldo}")
    
luis = CuentaBancaria('Luis', 100)
luis.depositar(50)
luis.mostrar_saldo() #150
luis.retirar(149)
luis.mostrar_saldo() # 1
luis.retirar(2) # Fondos insufivientes, estas intentando sacar 2€ pero en la cuenta tienes sólo 1€

print(luis.__saldo) # Da erro porqe estás intentando acceder a un ATRIBUTO PRIBADO
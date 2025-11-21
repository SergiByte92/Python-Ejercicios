# ENCAPSULAMIENTO: Protege los atributos de una clase para evitar accesos no deseados
# TIPOS DE ATRIBUTOS:
#   PÚBLICOS: Se pueden leer/modificar desde fuera sin restricción
#   PROTEGIDOS: (_atributo): Indica que NO se puede acceder directamente desde fuera
#   PRIVADOS: (_atributo) : NO accesible directamente desde fuera, Python los oculta internamente

class Coche:
    def __init__(self,marca,modelo,color):
        self.marca = marca # Atributo público
        self._modelo = modelo # Atributo protegido
        self.__color = color  # Atributo privado

    def conducir(self):
        print (f''' Conduciendo el coche:
               Marca: {self.marca}
               Modelo: {self._modelo}
               Color: {self.__color}''')

# Progama principal

if __name__ == "__main__":
    coche1 = Coche("Renaul", "Clio","Azul") # coche1 es un objeto. Coche es la clase
    coche1.conducir()

    print ("--------------------------------------------------")

    # Atributo público -> se puede modificar sin problemas
    coche1.marca ="Porche"
    coche1.conducir()

    print ("--------------------------------------------------")

    # Atributo protegido -> "en teoría", no se puede modificar, Python lo permite PERO NO ES UNA BUENA PRÁCTICA

    coche1._modelo ="Cayenne" # NO HACERLO
    coche1.conducir()

    print ("--------------------------------------------------")
"""
    # Atributo privado -> Como es un atributo privado, no te dejará

    coche1.__color = "Rojo"
    coche1.conducir()

    print ("--------------------------------------------------")

    # Linea que dará error: intentar leer un atributo privado directamente
    try:
        print(coche1.__color) # ERROR
    except ArithmeticError as e:
        print (f"ERROR 1: {e}")
    
    # Acceder a atributo privado con nombre mal formado

    try:
        print(coche1._Coche__Color)
    except AttributeError as e:
    print(f"ERROR 2:{e}")
"""
    

# Ejercicio: Crea la clase Perro con dos atributos: nombre y raza.
# Luego crea dos objetos distintos y muestra sus atributos mediante el método:  ladrar()
# De forma que salga: Mi perro <Toby> que es un <ladrador> está ladrando
# Realizar el diagrama de clase en notación UML

class Perro:
    def __init__(self, nombre, raza): # Método constructor
        self.nombre = nombre # Atributo
        self.raza = raza # Atributo
    
    def ladrar(self): # Metodo ladrar
        print(f"Mi perro {self.nombre} que es un {self.raza} está ladrando")

# Creo un objeto

firulais = Perro('Firulais','Pastor Alemán')
firulais.ladrar()

# Accedo a los atributos públicos de mi objeto
print (f" Mi perro {firulais.nombre} es un {firulais.raza}") # Atributos públicos (puedo acceder a ellos desde fuera de la clase)

# perro.ladrar() --> ERROR no has definido el objeto 'perro'
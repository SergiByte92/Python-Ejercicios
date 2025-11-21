
# Definición de UNA CLASE

# Una clase es como un molde o plantilla que describe como seran los objetos

class Persona: # Defimos la clase persona
    def __init__(self,nombre,apellido):
        # Método especial _init_() -> Es UN CONSTRUCTOR. Se ejecuta AUTOMÁTICAMENTE al crear el objeto
        # Se utiliza para inicializar los atributos de los objeto
        # 'Self' es una referencia al OBJETO que se está creando
        # nombre, apellido --> son parámetros que se pasan al objeto
        self.nombre = nombre
        self.apellido = apellido
    # Tenemos DOS ATRIBUTOS que son : nombre y apellido

    def mostrar_persona(self): # Em este método mostramos los dos atributos del objeto
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')

if __name__ == '__main__':
# Creamos objetos INVOCANDO a la clase Persona
# Primer objeto: persona1
    persona1 = Persona('Antonio','Rodríguez')
    
    persona1.mostrar_persona()

# Segundo objeto: olga
    olga = Persona('Olga','Pérez')
    olga.mostrar_persona()

# DIAGRAMA DE CLASES en notación UML
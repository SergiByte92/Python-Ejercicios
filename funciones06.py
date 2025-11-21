# docstring (documento string) --> ayuda interna que se utiliza para explicar que hace la función

def suma (a,b):
    """
        Suma de dos números y devuelve el resultado

        Párametros:
            a(int o float) : primer número
            b (int o float) : segundo número

        Devuelve:
            int o float : resultado de la suma    
    """
    return a+b

help(suma)
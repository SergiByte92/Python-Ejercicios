# Variable globales y locales

mensaje = " Hola...desde variable global"

def mostrar_mensaje():
    mensaje = " hola...desde la función  (variable local)"
    print(mensaje)

print(mensaje)
mostrar_mensaje()
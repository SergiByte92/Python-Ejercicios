# Solicitud de la introducción de datos al usuario.
# Asumimos que el usuario puede ser despistado y puede introducir espacios
# Captura, extension codesnap control shift + p

nombre_apellido=input("Introduzca su nombre y apellido : ").lower().replace(" ","")
empresa=input("introduzca su empresa: ").strip().lower()
dominio=".com".strip().lower()

correo= '@'.join([nombre_apellido,empresa+dominio])

print(f"Su correo asignado es el siguiente : {correo}" )
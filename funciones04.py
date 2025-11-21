# ALCANCE de las Variables globales y locales

cont_global = 0

def incrementar_contador():
    cont_local = 0
    global cont_global # con ' global ' indicamos que queremos acceder a la VARIABLE GLOBAL
    cont_global +=1
    cont_local +=1
    print(f"Contador local: {cont_local}")
    print(f"Contador local: {cont_global}")
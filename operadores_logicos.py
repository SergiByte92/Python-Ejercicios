""" tengo_dinero=True
tengo_vacaciones=False
if(tengo_dinero and tengo_vacaciones):
    print("Me voy a Cancun de vacaciones")
elif(tengo_dinero and not tengo_vacaciones):
    print("Me voy a comer cada dia al restaurante")
elif(not tengo_dinero and tengo_vacaciones):
    print("Me voy a casa de mis padres, no tengo dinero")
else : #not tengo_dinero and not tengo_vacaciones
    print("A currar...me he quedado sin vacaciones y sin dinero") """

tengo_dinero=False
tengo_vacaciones=False
if(tengo_dinero or tengo_vacaciones):
    print("Me voy a Cancun de vacaciones")
elif(tengo_dinero or not tengo_vacaciones):
    print("Me voy a comer cada dia al restaurante")
elif(not tengo_dinero or tengo_vacaciones):
    print("Me voy a casa de mis padres, no tengo dinero")
else : #not tengo_dinero and not tengo_vacaciones
    print("A currar...me he quedado sin vacaciones y sin dinero")

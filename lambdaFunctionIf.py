#Digita 2 numero e imprime el Mayor utilizando LAMBDA IF

nro1 = int(input("Digite el número uno: "))
nro2 = int(input("Digite el número dos: "))

numeroMayor = lambda x, y : True if nro1 > nro2 else False
print(numeroMayor(0,0))

if numeroMayor(nro1,nro2) == True:
    print("El número 1 es el número mayor")
elif numeroMayor(nro1,nro2) == False:
    print("El número 2 es el mayor")
else:
    print("Ambos número son iguales")
    





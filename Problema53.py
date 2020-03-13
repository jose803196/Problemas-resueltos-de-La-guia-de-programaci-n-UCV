#Jose G. Lopez
#Lenguaje : Python 2.7
#Problema 53

#Zona de funciones
def sumatoria(m):
	"""Esta funcion se encarga de sumar todos los numeros desde 1 hasta un numero dado por el usuario"""
	suma = ((m*(m+1))/2)
	return suma

#Zona del Programa Principal
#Rutina de pedido del dato
Comp = True
while(Comp == True):
	m = int(raw_input("Ingrese el numero: "))
	if (m > 0):
		Comp = False
		print(sumatoria(m))
	else:
		print("Tiene que ser un numero positivo")
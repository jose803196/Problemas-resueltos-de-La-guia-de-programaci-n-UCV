#Jose G. Lopez
#Lenguaje: Python 2.7
#Problema 1

#Zona de funciones
def x_1():
	"""Esta funcion se encarga de verificar el dato dado por el usuario."""	
	x = raw_input("Ingrese la coordenada x del punto: ")
	try:
		A = float(x)
		return A
	except ValueError:
		print("Ingrese datos numericos.")
def y_1():
	"""Esta funcion se encarga de verificar el dato dado por el usuario."""
	y = raw_input("Ingrese la coordenada y del punto: ")
	try:
		A = float(y)
		return A
	except ValueError:
		print("Ingrese datos numericos.")
def cuadrant(X,Y):
	"""Esta funcion se encarga de determinar el cuadrante en el cual se encuentra un punto."""
	if (X == 0) or (Y == 0):
		print("Este punto no define un cuadrante preciso.")
	elif (X > 0) and (Y > 0):
		print("El punto esta en el primer cuadrante.")
	elif (X < 0) and (Y > 0):
		print("El punto esta en el segundo cuadrante.")
	elif (X < 0) and (Y < 0):
		print("El punto esta en el tercer cuadrante.")
	else:
		print("El punto esta en el cuarto cuadrante.")
#Zona del programa pricipal
X = x_1()
Y = y_1()
Cua = cuadrant(X, Y)
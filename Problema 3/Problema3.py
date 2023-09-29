#Jose G. Lopez
#Lenguaje: Python 2.7
#Problema 3


import math
#Zona de funciones
def num_1():
	"""Esta funcion se encarga de verificar el dato dado como un numero."""
	x = raw_input("Ingrese la coordenada x del 1er punto: ")
	try:
		A = float(x)
		return A
	except ValueError:
		print("Ingrese datos numericos.")
def num_2():
	"""Esta funcion se encarga de verificar el dato dado como un numero."""
	y = raw_input("Ingrese la coordenada y del 1er punto: ")
	try:
		B = float(y)
		return B
	except ValueError:
		print("Ingrese datos numericos.")	
def num_3():
	"""Esta funcion se encarga de verificar el dato dado como un numero."""
	x = raw_input("Ingrese la coordenada x del 2do punto: ")
	try:
		C = float(x)
		return C
	except ValueError:
		print("Ingrese datos numericos.")
def num_4():
	"""Esta funcion se encarga de verificar el dato dado como un numero."""
	y = raw_input("Ingrese la coordenada y del 2do punto: ")
	try:
		D = float(y)
		return D
	except ValueError:
		print("Ingrese datos numericos.")
def longitud(A, B, C, D):
	"""Esta funcion se encarga de calcular la longitud de un punto a otro."""
	dx = C - A
	dy = D - B
	longi = math.sqrt((dx)**2 + (dy)**2)
	return longi
def puntmed(A, B, C, D):
	"""Esta funcion se encarga de calcular el punto medio entre los 2 puntos dados."""
	xmed = (C - A)/2
	ymed = (D - B)/2
	return "El punto medio es: {}, {}".format(xmed,ymed)
#Zona del progrma principal
A = num_1()
B = num_2()
C = num_3()
D = num_4()
E = longitud(A,B, C, D)
print(E)
F = puntmed(A, B, C, D)
print(F)
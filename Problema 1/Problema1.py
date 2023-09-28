
#Jose G. Lopez
#Lenguaje: Python 2.7
#Problema 1

import math
#Zona de funciones
def lposx():
	"""Esta funcion se encarga de demostrar que el dato ingresado sea numerico."""
	x = raw_input("Ingrese la coordenada x: ")
	try:
		x_1 = float(x)
		return x_1
	except(ValueError):
		print("Ingrese valores numericos")
		x_2 = lposx()

def lposy():
	"""Esta funcion se encarga de demostrar que el dato ingresado sea numerico."""
	y = raw_input("Ingrese la coordenada y: ")
	try:
		y_1 = float(y)
		return y_1
	except(ValueError):
		print("Ingrese valores numericos")
		y_2 = lposy()

def carapol(A, B):
	"""Esta funcion se encarga de transformar un numero de coordenadas cartesianas a polares."""
	r = math.sqrt((A)**2 + (B)**2)
	angulo = math.atan2(B, A)
	if A < 0 and B < 0:
		angulo_1 = 360+ math.degrees(angulo)
		return r,angulo_1
	elif A > 0 and B < 0:
		angulo_1 = 360 + math.degrees(angulo)
		return r, angulo_1
	elif A == 0 and B < 0:
		angulo_1 = 360 + math.degrees(angulo)
		return r, angulo_1
	else:
		angulo_1 = math.degrees(angulo)
		return r, angulo_1
#Zona del programa principal
A = lposx()
B = lposy()
C = carapol(A,B)
print(C)
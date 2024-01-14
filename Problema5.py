#Jose G. Lopez
#Lenguaje: Python 2.7.0
#Problema 5


import math
#Zona de funciones
def rad():
	"""Esta funcion se encarga de verificar el dato dado por el usuario"""
	r = raw_input("Ingrese el radio del cilindro: ")
	try:
		r_1 = float(r)
		if (r_1 >= 0):
			return r_1
		else:
			print("Ingrese valores positivos.")
			r_2 = rad()
	except ValueError:
		print("Por favor ingrese valores numericos.")
		r_2 = rad()

def alt():
	"""Esta funcion se encarga de verificar el dato dado por el usuario"""
	alt = raw_input("Ingrese la altura del cilindro: ")
	try:
		alt_1 = float(alt)
		if (alt_1 >= 0):
			return alt_1
		else:
			print("Ingrese valores positivos.")
			alt_2 = alt()
	except ValueError:
		print("Por favor ingrese valores numericos.")
		alt_2 = alt()

def volar(Rad, Alt):
	"""Esta funcion se encarga de calcular el volumen y area de el cilindro con los datos previamente dados por el usuario"""
	vol = ((math.pi)*(Rad)**2)*(Alt)
	are = (math.pi)*(Rad)**2
	return "El area es {}, y el volumen es {}".format(are,vol)
#Zona del programa pricipal
Rad = rad()
Alt = alt()
Volar = volar(Rad, Alt)
print(Volar)
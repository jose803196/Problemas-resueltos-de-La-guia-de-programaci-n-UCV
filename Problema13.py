#Jose G. Lopez
#Lenguaje : Python 2.7
#Problema 13

#Zona de funciones
import sys
def bisiesto(year):
	"""Esta funcion se encarga de comprobar si el año es bisiesto a traves de el calculo"""
	if (year % 4 == 0):
		return True
	else:
		return False

def secular(year):
	"""Esta funcion se encarga de comprobar si el año es secular a traves de otro calculo"""
	sec = ((year)%(400))
	if sec == 0:
		return True
	else:
		return False

def multiplo(year):
	"""Esta funcion se encarga de comprobar si el año dado es multiplo de 100"""
	multi = (year)%(100)
	if multi == 0:
		return True
	else:
		return False

#Zona del programa principal
Comp = True
while(Comp == True):
	year = int(raw_input("Ingrese el ano a estudiar: "))
	if year > 0:
		Comp = False
		if (multiplo(year) == True):
			if (secular(year) == True):
				print("El ano es secular (Es un ano bisiesto pero fin de siglo)")
			else:
				print("El ano no es secular")
		else:
			if (bisiesto(year) == True):
				print("El ano es bisiesto")
			else:
				print("El ano no es bisiesto")
	else:
		print("Vuelva a intentarlo.Por favor")
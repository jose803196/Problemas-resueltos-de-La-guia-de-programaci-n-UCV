#Jose G. Lopez
#Lenguaje: Python 2.7
#Problema 120
import numpy as np
import math
#Zona de funciones
def lenypos():
	"""Esta funcion se encarga de comprobar el orden de la matriz"""
	n = raw_input("Ingrese el orden de la matriz: ")
	try:
		n_1 = int(n)
		if (n_1 > 0):
			return n_1
		else:
			print("Debe ingresar un numero positivo.")
			return lenypos()
	except ValueError:
		print("Debe ingresar un numero entero.")
		return lenypos()
def componentes(i):
	"""Esta funcion se encarga de comprobar que los valores
		insertados sean numericos"""
	l = raw_input("Ingrese el valor a[{}][{}]: ".format(1,i+1))
	try:
		l_1 = float(l)
		return l_1
	except ValueError:
		print("Debe ingresar digitos y enteros.")
		return componentes(i)
#Zona del programa principal
n = lenypos()
p = int(n)
A = []
for i in range(0,p):
	m = componentes(i)
	A.append(m)
complemento = 0
for i in A:
	n = float(i)
	s = n**2
	complemento += s
norma = math.sqrt(complemento)
print(norma)
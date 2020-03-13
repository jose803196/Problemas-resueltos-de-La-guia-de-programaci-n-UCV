#Jose G. Lopez
#Lenguaje: Python 2.7
#Problema 42
import numpy as np
#Zona de funciones
def lenypos():
	n_1 = raw_input("Ingrese el numero: ")
	try:
		n_2 = int(n_1)
		if (n_2 > 0):
			return n_2
		else:
			print("Debe ingresar un numero positivo.")
			return lenypos()
	except ValueError:
		print("Debe ingresar un numero entero.")
		return lenypos()
#Zona del programa principal
n = lenypos()
A = []
for i in range(1,((n+1)/4)):
	lista_aux = []
	for j in range(1,((n+1)/4)):
		l = i*j
		if (i == j+1):
			lista_aux.append(l)
		else:
			lista_aux.append(0)
	A.append(lista_aux)
B = []
for i in A:
	for j in i:	
		if (j != 0):
			B.append(j)
		else:
			j += 1
for i in B:
	if (n == i):
		print("El numero dado es oblongo")
	else:
		i += 1

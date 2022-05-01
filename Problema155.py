#Jose G. Lopez
#Lenguaje: Python
#Problema 155
import numpy as np

#Zona de funciones
def row_comp():
	"""Regresa al usuario el valor de la fila"""
	while True:
		r = input("Ingrese el numero de filas: ")
		try:
			r_1 = int(r)
			if (r_1 > 1):
				return(r_1)
				break
			else:
				True
		except ValueError:
			print("Debe ingresar solo numeros enteros.")

def col_comp():
	"""Regresa al usuario el valor de la columna"""
	while True:
		c = input("Ingrese el numero de columnas: ")
		try:
			c_1 = int(c)
			if (c_1 > 1):
				return(c_1)
				break
			else:
				True
		except ValueError:
			print("Debe ingresar solo numeros enteros.")

def matrix_zz(row_1,col_1):
	"""Regresa al usuario la matriz NxM en zig-zag horizontal"""
	#Creo una matriz vacia y un contador
	A = []
	k = 1
	for i in range(0,row_1):
		lista_aux = []
		for j in range(0, col_1):
			lista_aux.append(k)
			k += 1
		if (i % 2 ) != 0:
			#Invierto las filas pares como en el ejemplo
			A.append(list(reversed(lista_aux)))
		else:
			A.append(lista_aux)
	return (A)
		

#Zona del programa principal
row_1 = row_comp()
col_1 = col_comp()
M = matrix_zz(row_1,col_1)
#Creo el ciclo for para que salga en orden la matriz en pantalla.
for i in M:
	print(i)
#Jose G. Lopez
#Lenguaje: Python
#Problema 161
import numpy as np

#Zona de Funciones

def orden():
	"""Devuelve una lista de dos terminos que es el orden de la matriz"""
	lista_orden = []
	while True:
		n = input("Ingrese el numero de filas: ")
		try:
			n_1 = int(n)
			if (n_1 > 1):
				lista_orden.append(n_1)
				break
			else:
				True
		except ValueError:
			print("Debe ingresar solo numeros enteros.")

	while True:
		n = input("Ingrese el numero de columnas: ")
		try:
			n_2 = int(n)
			if (n_2 > 1):
				lista_orden.append(n_2)
				break
			else:
				True
		except ValueError:
			print("Debe ingresar solo numeros enteros.")
	return(lista_orden)



def tart_glia(m,n):
	"""Regresa la matriz de Tartaglia"""
	#Creo la matriz de Tartaglia con solo valores de 1 y 0.
	T = []
	for i in range(m):
		lista_aux = []
		for j in range(n):
			if (i == 0) or (j == 0):
				lista_aux.append(1)
			else:
				lista_aux.append(0)
		T.append(lista_aux)

	#Inicio el procedimiento, lo que es realmente la suma
	for i in range(m):
		for j in range(n):
			if (i > 0) and (j > 0):
				T[i][j] = T[i-1][j] + T[i][j-1]
			else:
				pass
	#Solo importe la libreria numpy para el orden de la matriz T
	return(np.array(T))

#Zona del programa principal
l = orden()
#Tomo los valores veificados de l
m , n = l[0], l[1]
T = tart_glia(m,n)
print(T)
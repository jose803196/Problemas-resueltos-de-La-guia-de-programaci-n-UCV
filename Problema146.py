#Jose G. Lopez
#Lenguaje: Python 2.7
#Problema 146
import numpy as np
#Zona de funciones
def lenypos():
	"""Esta funcion se encarga de comprobar de que el numero dado sea positivo y entero"""
	Comp = True
	while(Comp == True):
		n = raw_input("Ingrese el numero de filas: ")
		try:
			n_1 = int(n)
			Comp = False
			Comp_2 = True
			while (Comp_2 == True):
				if (n_1 > 0):
					return n_1
				else:
					return lenypos()
		except ValueError:
			print("Ingrese valores numericos y enteros")

def lenypom():
	"""Esta funcion se encarga de comprobar de que el numero dado sea positivo y entero"""
	Comp = True
	while(Comp == True):
		n = raw_input("Ingrese el numero de columnas: ")
		try:
			n_1 = int(n)
			Comp = False
			Comp_2 = True
			while (Comp_2 == True):
				if (n_1 > 0):
					return n_1
				else:
					return lenypos()
		except ValueError:
			print("Ingrese valores numericos y enteros")

def matrices(n_2, m_2):
	"""Esta funcion se encarga del proceso de trasposicion y creacion de las matrices"""
	A_t = []
	for i in range(0, m_2):
		lista_aux = []
		for j in range(0,n_2):
			lista_aux.append(0)
		A_t.append(lista_aux)

	B = []
	for i in range(0, n_2):
		lista_aux = []
		for j in range(0,m_2):
			A_t[j][i] = raw_input("Ingrese el valor a[{}][{}]: ".format(i+1,j+1))
			A = A_t[j][i]
			lista_aux.append(A)
		B.append(lista_aux)
	print(np.array(B))
	return np.array(A_t)

#Zona del programa principal
n_2 = lenypos()
m_2 = lenypom()
A = matrices(n_2,m_2)
print(A)
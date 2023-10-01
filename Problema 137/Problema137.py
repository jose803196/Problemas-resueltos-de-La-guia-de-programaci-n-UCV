#Jose G. Lopez
#Lenguaje: Python 2.7
#Problema 137


#Zona de funciones
import numpy as np
#Creo al 1ra matriz
def lenypos_1():
	"""Esta funcion se encarga de que el numero dado sea positivo y entero"""
	Comp = True
	while(Comp == True):
		n = raw_input("Ingrese el numero de filas de la 1ra matriz: ")
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
def lenypom_1():
	"""Esta funcion se encarga de que el numero dado sea positivo y entero"""
	Comp = True
	while(Comp == True):
		n = raw_input("Ingrese el numero de columnas de la 1ra matriz: ")
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
def matriz_1(n_21, m_21):
	"""Esta funcion se encarga de crear la matriz A, y anadirle los valores"""
	A = []
	for i in range(0,n_21):
		lista_aux = []
		for j in range(0,m_21):
			k = raw_input("Ingrese el valor a[{}][{}]: ".format(i+1,j+1))
			lista_aux.append(k)
		A.append(lista_aux)
	return np.array(A)

#Creo la 2da matriz
def lenypos_2():
	"""Esta funcion se encarga de que el numero dado sea positivo y entero"""
	Comp = True
	while(Comp == True):
		n = raw_input("Ingrese el numero de filas de la 2da matriz: ")
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
def lenypom_2():
	"""Esta funcion se encarga de que el numero dado sea positivo y entero"""
	Comp = True
	while(Comp == True):
		n = raw_input("Ingrese el numero de columnas de la 2da matriz: ")
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
def matriz_2(n_22, m_22):
	"""Esta funcion se encarga de crear la matriz B, y anadirle los valores"""
	B = []
	for i in range(0,n_22):
		lista_aux = []
		for j in range(0,m_22):
			k = raw_input("Ingrese el valor a[{}][{}]: ".format(i+1,j+1))
			lista_aux.append(k)
		B.append(lista_aux)
	return np.array(B)

#Procedo a crear la 3 matriz y sumar la matriz A con la matriz B
def matriz_3(n_21, m_21, n_22, m_22):
	"""Esta funcion se encarga de crear la matriz resultante, a partir de las sumas de las 2 matrices anteriores"""
	if (n_21 == n_22) and (m_21 == m_22):
		C = []
		for i in range(0, n_21):
			lista_aux = []
			for j in range(0, m_21):
				A_1 = int(A[i][j])
				B_1 = int(B[i][j])
				m = A_1 + B_1
				lista_aux.append(m)
			C.append(lista_aux)
		return np.array(C)
	else:
		return "ADVERTENCIA: Los ordenes de la matrices no son iguales"

#Zona del programa principal
n_21 = lenypos_1()
m_21 = lenypom_1()
A = matriz_1(n_21,m_21)
n_22 = lenypos_2()
m_22 = lenypom_2()
B = matriz_2(n_22,m_22)
C = matriz_3(n_21, m_21, n_22, m_22)
print(C)
#Jose G. Lopez
#Lenguaje: Python
#Problema 147
#Zona de funciones
def Ord_A():
	"""Esta funcion se encarga de preguntar y validar el orden de la matriz"""
	ord_A = []
	for i in range(2):
		if (i == 0):
			s = True
			while(s == True):
				x = input("Ingrese el numero de filas de la matriz A: ")
				try:
					x_1 = int(x)
					if (x_1 > 0):
						ord_A.append(x_1)
						s = False
					else:
						s = True
				except ValueError:
					print("Debe ingresar solo numeros enteros.")
		else:
			s = True
			while(s == True):
				x = input("Ingrese el numero de columnas de la matriz A: ")
				try:
					x_1 = int(x)
					if (x_1 > 0):
						ord_A.append(x_1)
						s = False
					else:
						s = True
				except ValueError:
					print("Debe ingresar solo numeros enteros.")
	return(ord_A)

def Ord_B():
	"""Esta funcion se encarga de preguntar y validar el orden de la matriz"""
	ord_B = []
	for i in range(2):
		if (i == 0):
			s = True
			while(s == True):
				x = input("Ingrese el numero de filas de la matriz B: ")
				try:
					x_1 = int(x)
					if (x_1 > 0):
						ord_B.append(x_1)
						s = False
					else:
						s = True
				except ValueError:
					print("Debe ingresar solo numeros enteros.")
		else:
			s = True
			while(s == True):
				x = input("Ingrese el numero de columnas de la matriz B: ")
				try:
					x_1 = int(x)
					if (x_1 > 0):
						ord_B.append(x_1)
						s = False
					else:
						s = True
				except ValueError:
					print("Debe ingresar solo numeros enteros.")
	return(ord_B)

def Multicomp(ord_A, ord_B):
	"""Esta funcion se encargar de comprobar los ordenes de cada matriz y si es posible hacer su multiplicacion"""
	k_1 = int(ord_A[1])
	k_2 = int(ord_B[0])
	if (k_1 == k_2):
		return(True)
	else:
		return(False)

def MA(ord_A):
	"""Esta funcion se encarga de crear la matriz con los valores escritos por el usuario"""
	A = []
	n = ord_A[0]
	k_1 = ord_A[1]
	for i in range(0, n):
		lista_aux = []
		for j in range(0, k_1):
			s = True
			while(s == True):
				x = input("Ingrese el valor de a[{}][{}] de A: ".format(i+1,j+1))
				try:
					x_1 = float(x)
					lista_aux.append(x_1)
					s = False
				except ValueError:
					print("Debe ingresar numeros")
					s = True
		A.append(lista_aux)
	return(A)

def MB(ord_B):
	"""Esta funcion se encarga de crear la matriz con los valores escritos por el usuario"""
	B = []
	k_2 = ord_B[0]
	m = ord_B[1]
	for i in range(0, k_2):
		lista_aux = []
		for j in range(0, m):
			s = True
			while(s == True):
				x = input("Ingrese el valor de b[{}][{}] de B: ".format(i+1,j+1))
				try:
					x_1 = float(x)
					lista_aux.append(x_1)
					s = False
				except ValueError:
					print("Debe ingresar numeros")
					s = True
		B.append(lista_aux)
	return(B)

def Multim(A, B, ord_A, ord_B):
	"""Esta funcion se encarga de crear la matriz resultante de la multiplicacion, 
	multiplicar ambas matrices, y devolverlo en su respectiva matriz"""
	C = []
	for i in range(0, ord_A[0]):
		lista_aux = []
		for j in range(0, ord_B[1]):
			lista_aux.append(0)
		C.append(lista_aux)

	for i in range(ord_A[0]):
		for j in range(ord_B[1]):
			for k in range(ord_A[1]):
				C[i][j] += A[i][k] * B[k][j]
	return(C)

#Zona del Programa principal
ord_A = Ord_A()
ord_B = Ord_B()
multicomp = Multicomp(ord_A, ord_B)
if (multicomp == True):
	A = MA(ord_A)
	B = MB(ord_B)
	C = Multim(A, B, ord_A, ord_B)
	print(C)
else:
	print("No se puede hacer la multiplicacion de matrices")
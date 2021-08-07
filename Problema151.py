#Jose G. Lopez
#Lenguaje: Python
#Problema 151
import math
#Zona de funciones
def Ord_A():
	"""Esta funcion se encarga de preguntar y validar el orden de la matriz"""
	s = True
	while(s == True):
		x = input("Ingrese el orden de la matriz cuadrada A: ")
		try:
			x_1 = int(x)
			if (x_1 > 0):
				return(x_1)
				s = False
			else:
				s = True
		except ValueError:
			print("Debe ingresar solo numeros enteros.")

def MA(ord_A):
	"""Esta funcion se encarga de crear la matriz con los valores escritos por el usuario"""
	A = []
	n = ord_A
	for i in range(0,n):
		lista_aux = []
		for j in range(0, n):
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

def Nora(A, ord_A):
	"""Esta funcion se encarga de calcular la norma de la matriz dada mediante la suma total de cada fila; 
	ordenarlo a traves del metodo de la burbuja y escoger el ultimo valor ya que es el mayor y la norma de la matriz"""
	B = []
	for i in A:
		lista_aux = []
		for j in i:
			n = abs(j)
			lista_aux.append(n)
		c = sum(lista_aux)
		B.append(c)

	contador = 0
	while(contador != len(B)):
		Auxiliar = 0
		for i in range(0, len(B) - 1):
			Apuntador_1 = B[i]
			Apuntador_2 = B[i+1]
			if (Apuntador_1 > Apuntador_2):
				Auxiliar = Apuntador_2
				B[i+1] = B[i]
				B[i] = Auxiliar
			else:
				Apuntador_1 = B[i]
				Apuntador_2 = B[i+1]
		contador += 1
	b = len(B)
	return(B[b -1])
#Zona del Programa Principal
ord_A = Ord_A()
A = MA(ord_A)
Nora = Nora(A, ord_A)
print(Nora)
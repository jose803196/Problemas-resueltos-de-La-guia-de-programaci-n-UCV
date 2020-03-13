#Jose G. Lopez
#Lenguaje: Python 2.7
#Problema 32
#Zona funciones
def lentero_1():
	Comp_1 = True
	while(Comp_1 == True):
		a_1 = raw_input("Ingrese el primer numero: ")
		try:
			a_2 = int(a_1)
			if (a_2 > 0):
				return a_2
			else:
				return lentero()
		except ValueError:
			print("Debe ingresar un numero entero.")
def lentero_2():
	Comp_1 = True
	while(Comp_1 == True):
		b_1 = raw_input("Ingrese el segundo numero: ")
		try:
			b_2 = int(b_1)
			if (b_2 > 0):
				return b_2
			else:
				return lentero_1()
		except ValueError:
			print("Debe ingresar un numero entero.")
def divisores_1(A):
	c_1 = []
	for i in range(1,A):
		if ((A % i) == 0):
			c_1.append(i)
		else:
			c_1.append(0)
	return c_1
def divisores_2(B):
	d_1 = []
	for i in range(1,B):
		if ((B % i) == 0):
			d_1.append(i)
		else:
			d_1.append(0)
	return d_1
def Amismatica(A,B,C,D):
	e_1 = sum(C)
	e_2 = sum(D)
	if (e_1 == B) and (e_2 == A):
		return "Los dos numeros dados profesan amistad matematica."
	else:
		return "Los dos numeros dados no profesan amistad matematica."
#Zona del programa principal
A = lentero_1()
B = lentero_2()
C = divisores_1(A)
D = divisores_2(B)
E = Amismatica(A,B,C,D)
print(E)
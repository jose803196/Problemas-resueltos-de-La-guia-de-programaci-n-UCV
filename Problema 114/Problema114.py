#Jose G. Lopez
#Lenguaje: Python
#Problema 114
#Zona de funciones
def Comp_1():
	"""Esta funcion se encarga de pedir y coprobar el orden del vector A"""
	s = True
	while(s == True):
		x = input("Ingrese el numero de componentes de A: ")
		try:
			x_1 = int(x)
			if (x_1 > 0):
				return(x_1)
				s = False
			else:
				s = True
		except ValueError:
			print("Debe ingresar numeros.")
def Comp_2():
	"""Esta funcion se encarga de pedir y comprobar el orden del vector B"""
	s = True
	while(s == True):
		x = input("Ingrese el numero de componentes de B: ")
		try:
			x_1 = int(x)
			if (x_1 > 0):
				return(x_1)
				s = False
			else:
				s = True
		except ValueError:
			print("Debe ingresar numeros.")
def Arreg(comp_1, comp_2):
	"""Esta funcion se encarga de comparar el orden de los dos vectores dados
	para poder hacer o no el producto escalar"""
	if comp_1 == comp_2:
		return(True)
	else:
		return(False)
def MA(comp_1):
	"""Esta funcion se encarga de crear la matriz A y validar cada componente de ella"""
	A = []
	s = 1
	a = 1
	while(s <= comp_1):
		x = input("Ingrese el valor de a[1][{}] de A: ".format(a))
		try:
			x_1 = float(x)
			A.append(x)
			s += 1
			a += 1
		except ValueError:
			print("Debe ingresar numeros.")	
	return A
def MB(comp_1):
	"""Esta funcion se encarga de crear la matriz B y validar cada componente de ella"""
	B = []
	s = 1
	b = 1
	while(s <= comp_1):
		x = input("Ingrese el valor de b[1][{}] de B: ".format(b))
		try:
			x_1 = float(x)
			B.append(x)
			s += 1
			b += 1
		except ValueError:
			print("Debe ingresar numeros.")	
	return B
def pes(A,B):
	"""Esta funcion se encarga de hacer el producto escalar, despues de haber validado si se puede hacer o no."""
	Pes = []
	for i in range(0, comp_1):
		l = float(A[i])
		m = float(B[i])
		p = (l)*(m)
		Pes.append(p)
	Pes_1 = sum(Pes)
	return(Pes_1)
#Zona del programa principal
comp_1 = Comp_1()
comp_2 = Comp_2()
arreg = Arreg(comp_1, comp_2)
if(arreg == True):
	A = MA(comp_1)
	B = MB(comp_2)
	Pes = pes(A,B)
	print(Pes)
else:
	print("No se puede hacer el producto escalar")
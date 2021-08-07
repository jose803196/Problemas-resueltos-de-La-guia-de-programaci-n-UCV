#Jose G. Lopez
#Lenguaje: Python
#Problema 3
from numpy import array
#Zona de funciones
def x_data():
	"""xData = x_data.Se pide y verfica los  dos puntos dados."""
	x_list = []
	s = 1
	a = 1
	while(s <= 2):
		x = input("Ingrese el valor de x{}: ".format(a))
		try:
			x_1 = float(x)
			x_list.append(x_1)
			s += 1
			a += 1
		except ValueError:
			print("Debe ingresar numeros.")	
	return(array(x_list))
def y_data():
	"""yData = y_data.Se pide y se verifica los dos puntos dados."""
	y_list = []
	s = 1
	a = 1
	while(s <= 2):
		y = input("Ingrese el valor de y{}: ".format(a))
		try:
			y_1 = float(y)
			y_list.append(y_1)
			s += 1
			a += 1
		except ValueError:
			print("Debe ingresar numeros.")	
	return(array(y_list))
def x_sub():
	"""Esta funcion se encarga de pedir el valor de x para determinar el valor de la ordenada"""
	Comp = True
	while(Comp == True):
		x = input("Ingrese el valor de x para determinar y: ")
		try:
			x_1 = float(x)
			return(x_1)
			Comp = False
		except ValueError:
			print("Debe ingresar valores numericos.")
			Comp = True
def neville(xData, yData, x):
	"""p = neville(xData,yData,x) evalua el polinomio interpolado p(x) que pasa 
	el minimo especificado de los puntos dados por el metodo de Neville"""
	m = len(xData)	#Numero de puntos dados
	y = yData.copy()
	for k in range(1, m):
		y[0:m-k] = ((x - xData[k:m])*(y[0:m-k]) + (xData[0:m-k] - x)*(y[1:m-k+1]))/((xData[0:m-k]) - xData[k:m])
	return(y[0])
#Zona del programa principal
xData = x_data()
yData = y_data()
x = x_sub()
#Usare el metodo de Neville para la interpolacio lineal
a = neville(xData, yData, x)
print(a)
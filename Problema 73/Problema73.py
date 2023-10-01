#Jose G. Lopez
#Lenguaje: Python 2.7
#Problema 73
#Zona de funciones
def lenypos():
	"""Esta funcion se encarga de comprobar que el numero suministrado es entero y positivo"""
	a_1 = raw_input("Ingrese hasta que numero quiere la susecion: ")
	try:
		a_2 = int(a_1)
		if (a_2 > 0):
			return a_2
		elif (a_2 == 0):
			print("El cero no lo puede tomar.")
			return lenypos()
		else:
			print("Debe ingresar numeros positivos.")
			return lenypos()
	except ValueError:
		print("Debe ingrasar numeros enteros.")
		return lenypos()
def Fibonacci(A):
	"""Esta funcion se encarga de hacer la susecion Fibonacci"""
	a = 0
	b = 1
	Fibo = []
	for i in range(0,A):
		c = a + b
		Fibo.append(c)
		a = b
		b = c
	return Fibo
#Zona del programa prinipal
A = lenypos()
B = Fibonacci(A)
print(B)
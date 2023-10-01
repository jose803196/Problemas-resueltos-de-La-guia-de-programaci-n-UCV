#Jose G. Lopez
#Lenguaje: Python 2.7
#Problema 70

#Zona de funciones
def lentero():
	"""Esta funcion se encarga de validar el dato suministrado por el usuario, y comprobar
				que el mismo sea positivo y entero."""
	while True:
		n = raw_input("Ingrese el valor deseado: ")
		try:
			n_1 = int(n)
			return n_1
		except ValueError:
			print("POR FAVOR: Ingrese un valor numerico y entero")

def factorial(fac_1):
	"""Esta funcion se encarga de calcular el factorial de un numero."""
	contador = 1
	for i in range(1,fac_1 + 1):
		contador = (contador)*(i)
	return contador

#Zona del programa principal
Comp = True
while (Comp == True):
	fac_1 = lentero()
	if fac_1 < 0:
		print("POR FAVOR: Ingrese un valor positivo")
	elif (fac_1 == 0) or (fac_1 == 1):
		Comp = False
		print("El resultado es 1")
	else:
		Comp = False
		Factorial = factorial(fac_1)
		print(Factorial)
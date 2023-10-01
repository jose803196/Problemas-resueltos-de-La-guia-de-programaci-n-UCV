#Jose G. Lopez
#Lenguaje: Python
#Problema 47

#Zona de funciones
def num_1():
	"""Regresa al programa que el numero ingresado sea natural"""
	while True:
		n = input("Ingrese el numero N: ")
		try:
			n_1 = int(n)
			if (n_1 >= 0.0):
				return(n_1)
				break
			else:
				True
		except ValueError:
			print("Debe ingresar solo numeros enteros.")



def terpi_ta(N):
	"""Se encarga de contar cuantas ternas pitagoricas se forman por debajo del numero ingresado."""
	#Creo una variable que me contara cuantas veces se puede obtener una terna.
	Terna = 0
	#Creo un ciclo por debajo de N, empezando desde 0.
	for i in range(N):
		# iz_1 es la parte izquierda del Pitagoras.
		iz_1 = (i)**2 + (i+1)**2
		# de_1 es la parte derecha del Pitagoras.
		de_1 = (i+2)**2
		if (iz_1 == de_1):
			#Si las parte derecha y la izquierda son iguales, sumo a la terna
			Terna += 1
			return("Se forman {} ternas pitagóricas por debajo de {}".format(Terna,N))
		else:
			pass


#Zona del programa principal
N = num_1()
terna = terpi_ta(N)
print(terna)
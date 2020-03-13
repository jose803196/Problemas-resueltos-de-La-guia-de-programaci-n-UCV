#Jose G. Lopez
#Lenguaje: Python 2.7
#Problema 25
#Zona de funcines
def liscasi():
	"""Esta funcion se encarga de crear el tablero y cumple el enunciado"""
#Creacion del tablero y cantidad que hay en cada casilla
	A = []
	a = 1
	k = 1
	for i in range(0,8):
		lista_aux = []
		for j in range(0,8):
			if (i == 0) and (j == 0):
				lista_aux.append(a)
				print("En la casilla {}: {}".format(k, a))
			else:
				k += 1
				b = 2*a
				a = b
				print("En la casilla {}: {}".format(k, b))
				lista_aux.append(b)
		A.append(lista_aux)
#Creacion de la lista de la suma hasta la casilla n

	cont = 0
	k = 0
	for i in A:
		for j in i:
			k += 1
			cont += j
			print("En la casilla {}: {}".format(k, cont))
#Zona del programa principal
A = liscasi()
print(A)

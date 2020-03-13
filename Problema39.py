#Jose G. Lopez
#Lenguaje: Python 2.7
#Problema 39

#Zona de funciones
def lenypos():
	"""Esta funcion se encarga de que el numero dado sea positivo y entero"""
	Comp = True
	while(Comp == True):
		n = raw_input("Ingrese el numero: ")
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
def cubica(nar):
	"""Esta funcion se encarga de elevar al cubo cada digito dado e indicar que el numero es narcisista"""
	cb = str(nar)
	n_lista = []
	for i in cb:
		n_lista.append(i)
	cb_1 = len(cb)
	n_lista2 = []
	for i in n_lista:
		cubo = int(i)
		cub = (cubo)**(cb_1)
		n_lista2.append(cub)
	cb_2 = sum(n_lista2)
	if (nar == cb_2):
		return "El numero elegido es narcisista"
	else:
		return "El numero elegido no es narcisista"
#Zona del programa principal
nar = lenypos()
narc = cubica(nar)
print(narc)
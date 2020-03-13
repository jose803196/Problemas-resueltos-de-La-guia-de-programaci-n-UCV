#Jose G. Lopez
#Lenguaje: Python 2.7
#Problema 29

#Zona de funciones
def lentero():
	Comp_1 = True
	while (Comp_1 == True):
		n = raw_input("Ingrese el numero deseado: ")
		try:
			n_2 = int(n)
			Comp_2 = True
			while (Comp_2 == True):
				if (n_2 > 0):
					return n_2
				else:
					return lentero()
		except ValueError:
			print("ADVERTENCIA:Tiene que ingresar un numero entero.")
def divisores(n_1):
	A = []
	for i in range(1,n_1):
		if ((n_1%i) == 0):
			A.append(i)
		else:
			A.append(0)
	return(A)
def nufecto(B, n_1):
	D = sum(B)
	if (D == n_1):
		return "El numero es perfecto."
	else:
		return "El numero no es perfecto"
#Zona del programa principal
n_1 = lentero()
B = divisores(n_1)
C = nufecto(B,n_1)
print(C)
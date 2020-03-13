#Jose G. Lopez
#Lenguaje: Python 2.7
#Problema 33
#Zona de funciones
def lenypos_1():
	a_1 = raw_input("Ingrese el 1er numero: ")
	try:
		a_2 = int(a_1)
		if (a_2 > 0):
			return a_2
		else:
			print("Debe ingresar numeros positivos.")
			return lenypos_1()
	except ValueError:
		print("Debe ingresar valores numericos y enteros.")
		return lenypos_1()
def lenypos_2():
	b_1 = raw_input("Ingrese el 2do numero: ")
	try:
		b_2 = int(b_1)
		if (b_2 > 0):
			return b_2
		else:
			print("Deve ingresar numeros positivos.")
			return lenypos_2()
	except ValueError:
		print("Debe ingresar valores numericos y enteros.")
		return lenypos_2()
def amisdratica(A, B):
	c_1 = A**2
	c_2 = B**2
	c_3 = str(c_1)
	c_4 = str(c_2)
	c_5 = []
	c_6 = []
	for i in c_3:
		c_5.append(i)
	for j in c_4:
		c_6.append(j)
	
	d_1 = 0
	for i in c_5:
		l = int(i)
		d_1 += l
	d_2 = 0
	for j in c_6:
		m = int(j)
		d_2 += m
	if (A == d_2) and (B == d_1):
		return "Los numeros dados profesan amistad cuadratica"
	else:
		return "Los numeros dados no profesan amistad cuadratica"

#Zona del programa principal
A = lenypos_1()
B = lenypos_2()
C = amisdratica(A, B)
print(C)
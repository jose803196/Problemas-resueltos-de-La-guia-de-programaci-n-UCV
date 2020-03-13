#Jose G. Lopez
#Lenguaje : Python 2.7
#Problema 79

from fractions import Fraction
comprobacion = True 
while(comprobacion == True):
	n = int(raw_input("Ingrese hasta el numero entero y positivo hasta cual quiere la sumatoria: "))
	if n > 0:
		comprobacion = False
		resultado = 0
		for i in range(1,n+1):
			resultado += Fraction(1,i)
		print(resultado)
	else:
		print("El numero ingresado no es un entero positivo.Vuelva a intentarlo nuevamente")
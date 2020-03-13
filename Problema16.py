#Jose G. Lopez
#Lenguaje : Python 2.7
#Problema 16

#Rutina de pedido de dato
metros = float(raw_input("Ingrese el numero que desea transformar: "))

#Muestro las conversiones
print("1:Almud\n2:Cana\n3:Dedo\n4:Estadal\n5:Jarocha\n6:Palmo\n7:Mecate")
unity = int(raw_input("Marque la unidad que desea: "))


#Instancio las condiciones
comprobacion = True
while(comprobacion == True):
	if unity == 1:
		comprobacion = False
		Al = (metros)/(0.27)
		print("Su conversion es {} metros --> {}".format(metros,Al))
	elif unity == 2:
		comprobacion = False
		Ca = (metros)/(1.541)
		print("Su conversion es {} metros --> {}".format(metros,Ca))
	elif unity == 3:
		comprobacion = False
		De = (metros)/(0.0174)
		print("Su conversion es {} metros --> {}".format(metros,De))
	elif unity == 4:
		comprobacion = False
		Es = (metros)/(3.391)
		print("Su conversion es {} metros --> {}".format(metros,Es))
	elif unity == 5:
		comprobacion = False
		Ja = (metros)/(4.19)
		print("Su conversion es {} metros --> {}".format(metros,Ja))
	elif unity == 6:
		comprobacion = False
		Pal = (metros)/(0.212)
		print("Su conversion es {} metros --> {}".format(metros,Pal))
	elif unity == 7:
		comprobacion = False
		Me = (metros)/(20.062)
		print("Su conversion es {} metros --> {}".format(metros,Me))
	else:
		comprobacion = True
		print("Su numero debe estar entre 1 y 7")
		break
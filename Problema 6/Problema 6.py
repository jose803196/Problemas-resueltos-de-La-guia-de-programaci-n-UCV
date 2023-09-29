#Jose G. Lopez
#Lenguaje: Python 2.7
#Problema 6
import math
#Zona de funciones:
def Cilindricas(x, y, z):
	"""Esta funcion se encarga de transformar un punto de coordenadas cartesianas a coordenadas cilindricas"""
	if (x==0) and (y==0) and (x==0):
		print("El punto en coordenadas cilindricas es: ({},{},{})".format(x,y,z))
	elif (x == 0) and ( y > 0):
		print("El punto en coordenadas cilindricas es: ({},90,{})".format(y,z))
	elif (x == 0) and (y < 0):
		print("El punto en coordenadas cilindricas es: ({},270,{})".format(y,z))
	elif (y == 0) and (x > 0):
		print("El punto en coordenadas cilindricas es: ({},0,{})".format(x,z))
	elif (y == 0) and (x < 0):
		print("El punto en coordenadas cilindricas es: ({},180,{})".format(x,z))
	elif (x > 0 ) and (y > 0):
		r = math.sqrt((x**2) + (y**2))
		Angulo = math.atan(y/x)
		Angulo1 = math.degrees(Angulo)
		print("El punto en coordenadas cilindricas es: ({},{},{})".format(r,Angulo1,z))
	elif (x < 0) and (y > 0):
		r = math.sqrt((x**2) + (y**2))
		Angulo = math.atan(y/x)
		Angulo1 = math.degrees(Angulo)+180
		print("El punto en coordenadas cilindricas es: ({},{},{})".format(r,Angulo1,z))
	elif (x < 0) and (y < 0):
		r = math.sqrt((x**2) + (y**2))
		Angulo = math.atan(y/x)
		Angulo1 = math.degrees(Angulo) + 180
		print("El punto en coordenadas cilindricas es: ({},{},{})".format(r,Angulo1,z))
	elif (x > 0) and (y < 0):
		r = math.sqrt((x**2) + (y**2))
		Angulo = math.atan(y/x)
		Angulo1 = math.degrees(Angulo) + 360
		print("El punto en coordenadas cilindricas es: ({},{},{})".format(r,Angulo1,z))

def Esfericas(x, y, z):
	"""Esta funcion se encarga de transformar un punto de coordenadas cartesianas a coordenadas esfericas"""
	if (x > 0) and (y > 0):
		ro = math.sqrt((x**2)+(y**2)+(z**2))
		Teta = math.atan(y/x)
		Teta1 = math.degrees(Teta)
		Fi = math.atan(z/y)
		Fi1 = math.degrees(Fi)
		print("El punto en coordenadas esfericas es: ({}, {}, {})".format(ro,Teta1,Fi1))
	elif (x < 0) and (y > 0):
		ro = math.sqrt((x**2)+(y**2)+(z**2))
		Teta = math.atan(y/x)
		Teta1 = math.degrees(Teta)+180
		Fi = math.atan(z/y)
		Fi1 = math.degrees(Fi)
		print("El punto en coordenadas esfericas es: ({}, {}, {})".format(ro,Teta1,Fi1))
	elif (x < 0) and (y < 0):
		ro = math.sqrt((x**2)+(y**2)+(z**2))
		Teta = math.atan(y/x)
		Teta1 = math.degrees(Teta)+180
		Fi = math.atan(z/y)
		Fi1 = math.degrees(Fi)
		print("El punto en coordenadas esfericas es: ({}, {}, {})".format(ro,Teta1,Fi1))
	elif (x > 0) and (y < 0):
		ro = math.sqrt((x**2)+(y**2)+(z**2))
		Teta = math.atan(y/x)
		Teta1 = math.degrees(Teta)+360
		Fi = math.atan(z/y)
		Fi1 = math.degrees(Fi)
		print("El punto en coordenadas esfericas es: ({}, {}, {})".format(ro,Teta1,Fi1))
#Zona del programa principal:

x = float(raw_input("Ingrese la coordenada x del punto: "))
y = float(raw_input("Ingrese la coordenada y del punto: "))
z = float(raw_input("Ingrese la coordenada z del punto: "))
C = Cilindricas(x,y,z)
E = Esfericas(x,y,z)
print(C)
print(E)

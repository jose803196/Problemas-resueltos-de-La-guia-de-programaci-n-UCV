#Jose G. Lopez
#Lenguaje : Python 2.7
#Problema 57

H = float(raw_input("Ingrese la altura desde la cual cae la pelota: "))
Lim = 10**(-4)
h = H*(0.32)
Dist = H
while (h > Lim):
	Dist += 2*h
	h = h*(0.32)
print(Dist)
#Jose G. Lopez
#Lenguaje: Python 2.7
#Problema 119

#Rutina de creacion de matriz
import numpy as np
n = raw_input("Ingrese orden: ")
m = int(n)
A = np.zeros(m)
#Rutina de llenado de matriz
B = []
for i in A:
	l = raw_input("Ingrese los valores de la matriz: ")
	l_1 = int(l)
	B.append(l_1)
print(np.array(B))
#Rutina de media aritmetica
C = sum(B)
Media = C/m
print(Media)
#Jose G. Lopez
#Lenguaje: Python 2.7
#Problema 64

#Rutina de pedida de datos
import sys
H = float(raw_input("Ingrese la altura del pozo: "))
Ld = float(raw_input("Ingrese distancia de ascenso durante el dia del caracol: "))
Ln = float(raw_input("Ingrese distancia de descenso durante la noche del caracol: "))

#Rutina de condiciones
if (Ln > Ld):
	print("La distancia de descenso es mayor que la de ascenso, por lo tanto el caracol no saldra")
elif (Ld == Ln):
	print("El caracol no asciende ya que la distancia de ascenso es igual a la de descenso")
else:
	h = 0
	days = 0
	while(h < H):
		h += Ld
		days += 0.5
		if (h < H):
			h -= Ln
			days += 0.50

print("El caracol sale del pozo en: {}".format(days))
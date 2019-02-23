import math

a=int(input("ingresar valor a"))
b=int(input("ingresar valor b"))
c=int(input("ingresar valor c"))

d=b*b-4*a*c

if a!=0:
	if d<0:
		print("entonces no existe solución en los números reales")
	else:
		x1=(-b+(math.sqrt(d)))/(2*a)
		x2=(-b-(math.sqrt(d)))/(2*a)
		print("x1 = "+str(x1)+" x2 = "+str(x2))
else:
	print("coeficioente a debe ser diferente de cero")

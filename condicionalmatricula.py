#En una escuela el costo de matrícula de los alumnos se determina según el número de materias 
#que cursan. El costo de todas las materias es el mismo.
#Se ha establecido un programa para estimular a los alumnos, el cual consiste en lo siguiente: 
#si el promedio obtenido por un alumno en el último periodo es mayor o igual que 4,5, se le hará 
#un descuento del 30 % sobre la matrícula y no se le cobrara IVA; si el promedio obtenido es menor 
#que 4,5 deberá pagar la matrícula completa, la cual incluye el 10 % de IVA. Obtener cuánto debe 
#pagar un alumno.

print("**costo matricula**")
numero_materias = int(input("ingrese el numero de materias a cursar "))

costo_matricula = (numero_materias*10000)

print("costo de su matricula es: ",(costo_matricula))

promedio = int(input("ingrese su promedio"))

if(promedio>45):
    descuento = costo_matricula-((costo_matricula/100)*30)
    print("total a pagar: ",(costo_matricula-descuento))
else:
    iva = (costo_matricula/100)*10
    print("total a pagar: ",(costo_matricula+iva))
puntos = int(input("ingrese el promedio de IMEGA en la semana "))
ganancias = int(input("ingrese el monto total de las ganancias semanal "))

if(puntos>170):
    print("ha obtenido una sancion")
    print("total a pagar de multa",(ganancias/2))
else:
    print("felicidades")


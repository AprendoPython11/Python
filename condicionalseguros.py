#Una compañía de seguros está abriendo un departamento de finanzas y estableció un programa para captar 
#clientes, que consiste en lo siguiente: Si el monto por el que se efectúa la fianza es menor que 
#$500.000 la cuota a pagar será por el 3% del monto, y si el monto es mayor que $500.000 la cuota 
#a pagar será el 2% del monto. La afianzadora desea determinar cuál será la cuota que debe pagar un 
#cliente.

monto = int(input("ingrese el valor de su monto"))


if(monto<500000):
    print("total a pagar: ",(monto/100)*3)
else:
    print("total a pagar: ",(monto/100)*2)

#Una persona desea iniciar un negocio, para lo cual piensa verificar cuánto dinero le prestará el 
#banco por hipotecar su casa. Tiene una cuenta bancaria, pero no quiere disponer de ella a menos que 
#el monto por hipotecar su casa sea muy pequeño. Si el monto de la hipoteca es menor que $100’000.000 
#entonces invertirá el 50 % de la inversión total y un socio invertirá el otro 50 %. Si el monto de la 
#hipoteca es de $100’000.000 o más, entonces invertirá el monto total de la hipoteca y el resto del 
#dinero que se necesite para cubrir la inversión total se repartirá a partes iguales entre el socio y él.

monto = int(input("ingrese el valor del monto de la hipoteca "))
inversion = int(input("ingrese el valor de su inversion "))
if(monto<100000000):
    totali = (inversion/100)*50
    print("el total a pagar es: ",totali)
    print("el total a pagar de su socio es: ",totali)
else:
    inversion_total = inversion-monto
    total = inversion_total/2
    inversion = monto

    print("la inversion total tiene un valor de: ",inversion)
    print("el valor a pagar del restante es: ",total)
    print("el valor a pagar de su socio del restante es: ",total)
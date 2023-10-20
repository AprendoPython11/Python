#Una empresa de bienes raíces ofrece casas de interés social, bajo las siguientes condiciones: Si los ingresos 
#del comprador son menores de $800.000  la cuota inicial será del 15 % del costo de la casa y el 
#resto se distribuirá en pagos mensuales, a pagar en diez años. Si los ingresos del comprador son de 
#$800.000 o más la cuota inicial será del 30 % del costo de la casa y el resto se distribuirá en pagos 
#mensuales a pagar en 7 años.La empresa quiere obtener cuánto debe pagar un comprador por concepto 
#de cuota inicial y cuánto por cada pago parcial.

costo_casa = int(input("ingrese el valor de la casa"))
ci = int(input("ingrese el valor de sus ingresos"))

if(ci<800000):
    cuota_parcial = costo_casa/120
    descuento_inicial = (costo_casa/100)*15
    print("el valor de su cuota inicial es: ",(descuento_inicial))
    print("el valor de sus cuotas parciles es: ",cuota_parcial)
else:
    cuota_parcial = costo_casa/84
    descuento_inicial = (costo_casa/100)*30
    print("el valor de su cuota inicial es: ",(descuento_inicial))
    print("el valor de sus cuotas parciles es: ",cuota_parcial)

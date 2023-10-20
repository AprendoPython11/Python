#Calcular el total que una persona debe pagar en una llantería, si el precio de 
#cada llanta es de $80.000 si se compran menos de 5 llantas y de $70.000 si se compran 5 o más.

print("Bienvenido a llanteria")
can = int(input("ingrese la cantidad que desea comprar "))

if(can<5):
    print("total a pagar: ",(can*80000))
else:
    print("total a pagar: ",(can*70000))
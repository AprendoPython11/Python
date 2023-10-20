#En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento 
#dependiendo de un número de dos cifras que se escoge al azar. Si el número escogido es menor que
# 74 el descuento es del 15 % sobre el total de la compra, si es mayor o igual a 74 el descuento es
# del 2 0%. Obtener cuánto dinero se le descuenta.

print("prueba tu suerte en nuestra promocion")
numr = int(input("ingresa un numero de 2 cifras"))

if(numr<74):
    print("su descuento es del 15%")
    compra = int(input("ingrese el valor de su  compra"))
    print("su descuento tiene un valor de: ",(compra/100)*15)
else:
    if(numr>=74):
        print("su descuento es de 20%")
        compra = int(input("ingrese el valor de su  compra"))
        print("su descuento tiene un valor de: ",(compra/100)*20)

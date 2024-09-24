# Hacer un programa que simule un cajero automático con un saldo inicial de $1000 y tendrá el siguiente menú de opciones: 
# 1. Ingresar dinero en la cuenta
# 2. Retirar dinero de la cuenta
# 3. Mostrar dinero disponible
# 4. Salir

dinero = 1000

op = int(input("---Bienvenido a NataBanck-----  \n"
      "1. Ingresar dinero en la cuenta \n"
      "2. Retirar dinero de la cuenta \n" 
      "3. Mostrar dinero disponible \n 4. Salir \n"))

if op == 1:
    bono = int(input("Ingrese el valor a agregar a su cuenta: "))
    if bono <= 0:
      print("Ingreso un valor no valido, por favor vuelve a intentarlo")
    else: 
      print(f"Total valor en la cuenta ${dinero + bono}")

if op == 2:
    retiro = int(input("Ingrese el valor a retirar de su cuenta: "))
    if (retiro <= 0):
      print("Ingreso un valor no valido, por favor vuelve a intentarlo")
    elif (retiro > 1000):
       print("Fondos insuficientes")
    else: 
      print(f"Total valor en la cuenta ${dinero - retiro}")

if op == 3:
      print(f"Total valor en la cuenta ${dinero}")

if op == 4:
      print("Regresa pronto")
   
   


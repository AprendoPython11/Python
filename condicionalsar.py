#El gobierno ha establecido el programa SAR (Sistema de Ahorro para el Retiro) que consiste en 
#que los dueños de la empresa deben obligatoriamente depositar en una cuenta bancaria un porcentaje 
#del salario de los trabajadores; adicionalmente los trabajadores pueden solicitar a la empresa que 
#deposite directamente una cuota fija o un porcentaje de su salario en la cuenta del SAR, la cual le 
#será descontada de su pago.
#Un trabajador que ha decidido aportar a su cuenta del SAR desea saber la cantidad total de dinero 
#que estará depositado a esa cuenta cada mes, y el pago mensual que recibirá.

salario = int(input("ingrese el valor de su salario"))
porcentaje = int(input("ingrese el porcentaje que desea aportar"))

valor_pension = (salario/100)*porcentaje
valor_salario = salario-valor_pension

print("el valor total del aporte es: ",valor_pension,"\n","el valor total de su salario es: ",valor_salario)

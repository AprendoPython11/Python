#Una persona se encuentra con un problema de comprar un automóvil o un terreno, los cuales cuestan 
#exactamente lo mismo. Sabe que mientras el automóvil se devalúa, con el terreno sucede lo contrario. 
#Esta persona comprara el automóvil si al cabo de tres años la devaluación de este no es mayor que 
#la mitad del incremento del valor del terreno. Ayúdale a esta persona a determinar si debe o no 
#comprar el automóvil.

valor_automivil = int(input("ingrese el valor del automivil "))
valor_devaluacion = int(input("ingrese el valor de la devaluacion del automivil "))
valor_incremento = int(input("ingrese el valor del incremento del terreno "))

if(valor_devaluacion<(valor_incremento/2)):
    print("puedes comprar el automovil")
else:
    print("no deberias comprar el autovil")
#Calcular el número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico;
# la fórmula que se aplica cuando el sexo es femenino es:

edad = int(input("ingrese su edad "))
sexo = int(input("ingrese su genero 1 para femenino 2 para masculino "))

if(sexo==1):
    num_pulsaciones = (220-edad)/10
    print("su numero de pulsaciones : ",num_pulsaciones)
else:
    num_pulsaciones = (210-edad)/10
    print("su numero de pulsaciones : ",num_pulsaciones)


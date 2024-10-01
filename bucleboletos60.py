# Tienes 100 boletos para una rifa benéfica y cada cliente puede comprar entre 1 y 5 boletos, 
# pero solo se puede vender un máximo de 10 boletos a personas mayores de 60 años. 
# El sistema debe registrar el nombre, edad y la cantidad de boletos comprados por cada cliente, 
# asegurándose de que no se vendan más de 10 boletos a personas de más de 60 años y que el total de boletos no exceda los 100 disponibles. 
# Al final, el programa debe mostrar cuántas personas compraron exactamente 5 boletos, cuántos boletos fueron vendidos a 
# personas mayores de 60 años, el cliente que compró más boletos y el promedio de boletos vendidos por persona. 

customers = []
boletos = 40
personas_5_boletos = 0
boletos_ventidos_60 = 0
nombre_persona_mas_boletos = None
mas_boletos = 0

while boletos > 0:
    nombre = input("Ingresa por favor tu nombre ")
    edad = int(input("Ingrese su edad "))
    cantidad_boletos = int(input("Ingrese cantidad de boletos "))

    if 1 < cantidad_boletos > 5 and edad < 60:
        print("Solo se permiten de 1 a 5 boletos")
        continue

    if edad >= 60 and cantidad_boletos > 10:
        print("Solo se permite maximo 10 boletos")
        continue

    if cantidad_boletos > boletos:
        print(f"lo siento pero solo quedan estos boletos: {boletos}")
        continue
    
    if cantidad_boletos == 5:
        personas_5_boletos += 1

    if edad >= 60:
        boletos_ventidos_60 += cantidad_boletos
    
    if nombre_persona_mas_boletos is None or cantidad_boletos > mas_boletos:
        nombre_persona_mas_boletos = nombre
        mas_boletos = cantidad_boletos


    cliente = []
    cliente.append((nombre, edad, cantidad_boletos))
    customers.append(cliente)
    boletos -= cantidad_boletos
    print(boletos)

print(customers)
print(f"Total personas que compraron 5 boletos: {personas_5_boletos}")
print(f"Total boletos personas de 60: {boletos_ventidos_60}")
print(f"La persona que compró más boletos fue : {nombre_persona_mas_boletos} con {mas_boletos} boletos")
print(f"El promedio de la compra de boletos por persona es: {40/len(customers)}")
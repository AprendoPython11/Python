# Tienes un cupo de 20 tickets para un evento y cada persona puede comprar un máximo de 4 tickets. 
# El sistema debe registrar el nombre, edad y cantidad de tickets que compró cada persona, 
# y solo se permitirá la compra a personas mayores de 18 años. Además, el sistema debe validar que 
# la cantidad de tickets solicitados no exceda los disponibles y debe detenerse una vez que se hayan vendido todos los tickets. 
# Al final, el programa debe mostrar cuántas personas compraron exactamente 4 tickets, el total de personas registradas, 
# y el nombre de la persona más joven que haya comprado tickets

# el while nos sirve para cuando necesitemos evaluar una varialble y el for cuando ya sabemos el limite

stock_tikets = 20
customers = []
peronas_4_tikets = 0
nombre_joven = None
edad_joven = None

while(stock_tikets > 0):

    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    tikets = int(input("Ingresa la cantidad de tikest a comprar: "))

    # continue es para que el bucle no se estanque y continue 
    if(edad < 17):
        print("Es solo de venta a mayores de edad")
        continue
    
    if(tikets > 5): 
        print("solo se pueden comprar entre 1 y 4 tikets")
        continue

    if(stock_tikets == 0 or tikets > stock_tikets):
        print(f"Solo quedan esta cantidad de tikets: {stock_tikets}")
        continue

    # contador 
    if(tikets == 4):
        peronas_4_tikets += 1

    # si nombre_joven es None osea que está vacio asigna los valores
    # O si la nueva edad es menor que la que ya estaba esta se compara y luego se reemplaza
    if(nombre_joven is None or edad < edad_joven):
        nombre_joven = nombre
        edad_joven = edad

    usuario = []
    usuario.append((nombre,edad, tikets))
    customers.append(usuario)
    stock_tikets -= tikets
    print(stock_tikets)

print(customers)
print(f"la cantidad de personas registradas es: {len(customers)}")
print(f"perosnas que compraron 4 tokets: {peronas_4_tikets}")
print(f"la persona más joven registrar es: {nombre_joven}")

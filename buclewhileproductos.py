# Tienes un conjunto de 50 productos en una tienda y cada cliente puede comprar 
# un máximo de 10 productos. El sistema debe registrar el nombre, la edad y la cantidad de 
# productos comprados por cada cliente, asegurándose de que solo se permita la compra a personas 
# mayores de 21 años. El proceso se repite hasta que todos los productos se hayan vendido. 
# Al final, el programa debe mostrar cuántas personas compraron exactamente 10 productos, 
# el total de personas que compraron, y el nombre del cliente que compró la menor 
# cantidad de productos. 

clientes = []
productos = 20
menos_productos = None
nombre_menos_productos = None
productos_10 = 0


while(productos > 0):

    nombre_cliente = input("Enter your name: ")
    edad = int(input("Enter your age: "))

    if edad < 21:
        print("Only 21 years of age and older are allowed")
        continue

    num_productos = int(input("Enter the quatify to buy: "))
    
    if num_productos > 10:
        print(f"Sorry, you can only buy 10 products")
        continue
    
    if num_productos > productos:
        print(f"Sorry, only these products are left: {productos}")
        continue

    if num_productos == 10:
        productos_10 += 1
        
    
    if nombre_menos_productos is None or num_productos < menos_productos:
        nombre_menos_productos = nombre_cliente
        menos_productos = num_productos 

    customer = []
    customer.append((nombre_cliente, edad, num_productos))
    productos -= num_productos
    clientes.append(customer)
    print(productos)
    

print(clientes)
print(f"personas que compraron 10 productos fueron: {productos_10}")
print(f"el numero total de clientes fue de: {len(clientes)}")
print(f"la perosona que compró menos productos fue: {nombre_menos_productos}")
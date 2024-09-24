# Hacer un programa que pida 2 números y se de cuenta cuál de ellos es par, o si ambos lo son.

# Se piden los dos numero
num1 = int(input("Ingrese primer número "))
num2 = int(input("Ingrese segundo número "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("El numero ",num1, " y ", num2," son par") 
elif num1 % 2 == 0:
    print("El numero ", num1, " es par")
    print("El numero ", num2, " es impar")
elif num2 % 2 == 0:
    print("El numero ", num2, " es par")
    print("El numero ", num1, " es impar")
else:
    print("El numero ",num1, " y ", num2," son impar")


# Hacer un programa que pida 3 números y determine cuál es el mayor.

number = []

for i in range (3):
    num = int(input('Ingresa un número '))
    number.append(num)

print(f"De {number}")
print(f"El numero mayor es : {max(number)}")
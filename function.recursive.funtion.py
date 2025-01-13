n = int(input("Ingresa un numero "))

def funtion_number(n):
    if n == 0 or n == 1:
        return 1  # if n fit in the if condicion dont do the recursive call
    return n * funtion_number(n - 1)  # recursive call


print(funtion_number(n))

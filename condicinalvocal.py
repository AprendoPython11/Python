# Hacer un programa que pida un caracter y decir si es una vocal 

vocales = ["a", "e", "i", "o" , "u"]

letra = input("Enter a letter: ")

if len(letra) >= 2:
    print("Only one letter")
elif letra in vocales:
    print("It's a vowel")
else:
    print("It's a consonant")

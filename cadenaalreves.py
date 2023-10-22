# EN PYTHON
#Índices positivos: Los índices positivos en una cadena de texto representan la posición 
# del carácter en la cadena, comenzando desde 0 para el primer carácter 
# y así sucesivamente.

# Índices negativos: Los índices negativos representan la posición del carácter desde el final 
# de la cadena. -1 representa el último carácter, -2 representa el penúltimo carácter y así sucesivamente.

# Cortes de lista (start:stop:step):los cortes de lista son para extraer una subcadena de una cadena. 
# Si omites start=empieza e stop=termina y solo usas step=el tamaño del paso entre los elementos.

var = int(input("ingrese una numero "))

num = str(var)
var_al_reves = num[::-1]

print(var_al_reves)
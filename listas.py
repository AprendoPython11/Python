
# lista
dulces = ["dona", "pastel de arequipe","bombon", "chicle"]
print(dulces)

# lista dentro de otra lista
dulces = ["dona", "cookie","pastel de arequipe","bombon", "chicle",[1, 2, 3]]
print(dulces[-1])

# sublista
panaderia = dulces[1:3]
print(panaderia)

# para preguntar si un elemto está en la lista 
print("dona" in panaderia)

# lista dos veces
dulces = ["dona", "pastel de arequipe","bombon", "chicle"] * 2
print(dulces)

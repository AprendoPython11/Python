metros = int(input("ingrese el valor de los metros cuadrados del bosque"))

if(metros>1000000):
    mpinos = (metros/100)*70
    print("la cantidad que caben de pinos por cada 10 m2 es: ",(mpinos/10)*8)

    mroble = (metros/100)*20
    print("la cantidad que caben de robles por cada 15 m2 es: ",(mroble/15)*15)

    mcedro = (metros/100)*10
    print("la cantidad que caben de cedros por cada 18 m2 es: ",(mcedro/18)*10)

else:
    mpinos = (metros/100)*50
    print("la cantidad que caben de pinos por cada 10 m2 es: ",(mpinos/10)*8)

    mroble = (metros/100)*30
    print("la cantidad que caben de robles por cada 15 m2 es: ",(mroble/15)*15)

    mcedro = (metros/100)*20
    print("la cantidad que caben de cedros por cada 18 m2 es: ",(mcedro/18)*10)
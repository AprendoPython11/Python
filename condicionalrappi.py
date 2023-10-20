print("=======================================")
print("sistema de control de vaciones de rappi")
print("=======================================")

for i in range( 1, 6, 1):
    nomb = input("ingrese el nombre del empleado:")
    clave_depa = int(input("ingrese la clave del departamento:"))
    antigue_emple = int(input("ingrese los años laborados del empleado:"))


    if clave_depa == 1:
        acu_clave1 = 0
        acu_clave1 = acu_clave1 + 1
        if antigue_emple >= 1 and antigue_emple < 2:
            print("el empleado ", nomb, "tiene derechos a 6 dias de vacaciones")
        elif antigue_emple >= 2 and antigue_emple <=6:
            print("el empleado ", nomb, "tiene derechos a 14 dias de vacaciones")
        elif antigue_emple >= 7:
            print("el empleado ", nomb, "tiene derechos a 20 dias de vacaciones")
        else:
            print("el empleado ", nomb, "aun no tiene derecho a vacaciones.")


    elif clave_depa == 2:
        acu_clave2 = 0
        acu_clave2 = acu_clave2 + 1
        if antigue_emple >= 1 and antigue_emple < 2:
            acu1 = 0
            acu1 = acu1 + 1
            print("el empleado ", nomb, "tiene derechos a 7 dias de vacaciones")
        elif antigue_emple >= 2 and antigue_emple <=6: 
            acu2 = 0
            acu2 = acu2 + 1
            print("el empleado ", nomb, "tiene derechos a 15 dias de vacaciones")
        elif antigue_emple >= 7:
            acu3 = 0
            acu3 = acu3 + 1
            print("el empleado ", nomb, "tiene derechos a 22 dias de vacaciones")
        else:
            print("el empleado ", nomb, "aun no tiene derecho a vacaciones.")

    elif clave_depa == 3:
        acu_calve3 = 0
        acu_calve3 = acu_calve3 + 1 
        if antigue_emple >= 1 and antigue_emple < 2:
            print("el empleado ", nomb, "tiene derechos a 10 dias de vacaciones")
        elif antigue_emple >= 2 and antigue_emple <=6:
            print("el empleado ", nomb, "tiene derechos a 20 dias de vacaciones")
        elif antigue_emple >= 7:
            print("el empleado ", nomb, "tiene derechos a 30 dias de vacaciones")
        else:
            print("el empleado ", nomb, "aun no tiene derecho a vacaciones.")
    else:
        print("la clave del departamento no existe intentelo denuevo")


# total_porcentaje = (acu1/100)*100


total_porcentaje = (acu_clave1/6)*100
total_promedio  = (acu1 + acu2 + acu3)/3


print("el porcentaje de empleados con calve 1 es: ",total_porcentaje)
print("el promedo de empledos con clave 2 es: ",total_promedio)

# if total_suma_clave1 > total_suma_clave2:
#     if total_suma_clave1 > total_suma_clave3:
#         print("la clave maxima es: calve 1")
# elif total_suma_clave2 > total_suma_clave1:
#     if total_suma_clave2 > total_suma_clave3:
#         print("la clave maxima es: clave 2")
# else:
#     print("la clave maxima es: clave 3")


# if total_suma_clave1 < total_suma_clave2:
#     if total_suma_clave1 < total_suma_clave3:
#         print("la clave minima es: clave 1")
# elif total_suma_clave2 < total_suma_clave1:
#     if total_suma_clave2 < total_suma_clave3:
#         print("la clave minima es: cave 2")
# else:
#     print("la clave minima es: 3")





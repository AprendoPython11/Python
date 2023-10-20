print("=======================================")
print("sistema de control de vaciones de rappi")
print("=======================================")

nomb = input("ingrese el nombre del empleado:")
clave_depa = int(input("ingrese la clave del departamento:"))
antigue_emple = int(input("ingrese los años laborados del empleado:"))

if clave_depa == 1:
    if antigue_emple >= 1 and antigue_emple < 2:
        print("el empleado ", nomb, "tiene derechos a 6 dias de vacaciones")
    elif antigue_emple >= 2 and antigue_emple <=6:
        print("el empleado ", nomb, "tiene derechos a 14 dias de vacaciones")
    elif antigue_emple >= 7:
        print("el empleado ", nomb, "tiene derechos a 20 dias de vacaciones")
    else:
        print("el empleado ", nomb, "aun no tiene derecho a vacaciones.")

elif clave_depa == 2:
    if antigue_emple >= 1 and antigue_emple < 2:
        print("el empleado ", nomb, "tiene derechos a 7 dias de vacaciones")
    elif antigue_emple >= 2 and antigue_emple <=6:
        print("el empleado ", nomb, "tiene derechos a 15 dias de vacaciones")
    elif antigue_emple >= 7:
        print("el empleado ", nomb, "tiene derechos a 22 dias de vacaciones")
    else:
        print("el empleado ", nomb, "aun no tiene derecho a vacaciones.")

elif clave_depa == 3:
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
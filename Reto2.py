#invierno - enero feb mar
# primavera - arb may jun
# verano - jul ago spt
# otoño - oct nov dic


mesEstac = input("Digite el mes, del cual desea saber la estacion: ")
mes = mesEstac.lower()


if(mes == "enero" or mes == "febrero" or mesc == "marzo"):
    print(f'el mes ingresado {mes} pertenece a la estacion Inverno')

elif (mes == "abril" or mes == "mayo" or mesc == "junio"):
    print(f'el mes ingresado {mes} pertenece a la estacion primavera')

elif (mes == "julio" or mes == "agosto" or mesc == "septiembre"):
    print(f'el mes ingresado {mes} pertenece a la estacion verano')

elif (mes == "octubre" or mes == "noviembre" or mesc == "diciembre"):
    print(f'el mes ingresado {mes} pertenece a la estacion otoño')
else:
    print(f'ingrese una opcion valida')
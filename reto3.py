#de 0 a 14 niÃ±o
# 14 a 28 joven
# 28 a 60 adulto
# mayor a 60 adulto mayor


edad = int(input("Digite la edad de la persona: "))  


if ( edad>=0 and edad<14):   
    print(f'para la edad ingresada {edad} se encuentra en el nuvel de edad NIÃO ð¶ð½') 
elif (edad>=14 and edad<28):
    print(f'para la edad ingresada {edad} se encuentra en el nuvel de edad JOVEN ð§ð½')
elif (edad>=28 and edad<60):
    print(f'para la edad ingresada {edad} se encuentra en el nuvel de edad ADULTO ð§ð½')
elif ( edad>=60 and edad <=150):
    print(f'para la edad ingresada {edad} se encuentra en el nuvel de edad ADULTO MAYOR ð´ð½')
else:
    print(f'la edad ingresada no es valida intente nuevamente')
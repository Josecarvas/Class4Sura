# entre 0 y 20 estoy mal
# entre 20 y 400 estoy bin 
# si estoy por encima de 400 run ๐๐ง๐จ๐

# entrada  = variables = referencias en memoria

from ast import If


h20level = float(input("Digite el nivel de agua: "))  # las variables siempre en minusculas y se deben inicializar


# proceso  para colocar y se coloca and 
if ( h20level>=0 and h20level<20):   
    print(f'nivel de agua {h20level} BAJO - ๐งโ') # salida cada print es una salida
elif (h20level>=20 and h20level<400):
    print(f'nivel de agua {h20level} NORMAAAAL  - ๐๐ค') # salida cada print es una salida
elif ( h20level>=400):
    print(f' โ  ๐ ๐ฉฑ   nivel de agua {h20level} PELIGROSO RUNN  -  ๐ ๐จ โ ') # salida cada print es una salida
else:
    print(f'El nivel ingresado no es valido, intente nuevamente') # salida cada print es una salida


# salida cada print es una salida

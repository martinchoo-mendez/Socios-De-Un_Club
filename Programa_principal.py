from Función import buscar

Lista_socios=[9845, 1165, 987, 5297]
LIsta_estados=["vitalicio", "federado", "regular", "regular"]
Lista_años=[1975, 1983, 2010, 1970]
#estas solo son listas de ejemplos, el programa debe funcionar con cualquiera juego de listas que se correspondan.

numero_socio=int(input("ingrese número de socio: "))
indice=buscar(Lista_socios, numero_socio)
cuota=15000

if indice >-1:
    if Lista_años[indice]<=1980:
        descuento=(40/100)*cuota
        cuota-=descuento
        print("El estado del socio:", numero_socio, "es", LIsta_estados[indice], ". Año de ingreso es", Lista_años[indice],". Su cuota es de:$", cuota)
    elif Lista_años[indice]>1980 and Lista_años[indice]<=1990:
        descuento=(20/100)*cuota
        cuota-=descuento
        print("El estado del socio:", numero_socio, "es", LIsta_estados[indice], ". Año de ingreso es", Lista_años[indice],". Su cuota es de:$", cuota)
    else:
        print("El estado del socio:", numero_socio, "es", LIsta_estados[indice], ". Año de ingreso es", Lista_años[indice],". Su cuota es de:$", cuota)
else:
    print("Bienvenido al club, ¿desea asociarse?")
def calculo_bisiesto(anio):
    if (anio%4== 0):
        if anio%100 == 0:
            if anio%400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

anio = 1999
bisiesto = calculo_bisiesto(anio)

if bisiesto:
    print("El año", anio,"es bisiesto")
else:
    print("El año", anio,"no es bisiesto")

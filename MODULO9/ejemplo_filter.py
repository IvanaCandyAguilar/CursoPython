numeros =[1,2,3,4,5,6,7,8,9,10]

def mi_funcion(x):
    if x % 2 == 0:
        return True
    return False

def otra_funcion(x):
    if str(x).startswith('pep'):
        return True
    return False

#resultado = filter (mi_funcion,numeros)
#resultado = filter(lambda x: x % 2 == 0,numeros)
#resultado2 = filter(lambda x: str(x).startswith('pep'),['pepe','pepito','juan'])
resultado2 = filter(otra_funcion,['pepe','pepito','juan'])
print(list(resultado2))

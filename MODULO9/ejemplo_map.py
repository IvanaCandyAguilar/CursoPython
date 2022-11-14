# la funcion necesita un solo parametro
# devuelve una lista
def cuadrado(x):
    return x*x

#resultado = map(cuadrado,[1,2,3,4,5,6,7,8,9,10])
resultado = map(lambda x: x*x,[1,2,3,4,5,6,7,8,9,10])
print(list(resultado))


from functools import reduce
#las funciones con reduce necesita dos parametros
# un solo resultado ejemplo fibonaci
# puede servir para contar palabras de un texto

def suma(a, b):
    return a+b

lista = [1,2,3,4,5]
#res = reduce(suma,lista)

res = reduce(lambda a,b: a+b , lista)

print(res)

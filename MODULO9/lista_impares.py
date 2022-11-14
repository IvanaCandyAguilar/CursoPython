from functools import reduce

def suma(a,b):
    return a+b

def main():
    numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    print('Lista de números',numeros)
    impares = list(filter(lambda x: x % 2 == 1, numeros))

    suma_total = reduce(suma, impares)
    print('Lista de impares',impares)
    print('Suma total',suma_total)


if __name__ == '__main__':
    main()

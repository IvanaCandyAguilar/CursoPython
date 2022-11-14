secreto = 50
#valor = input('Introcuce un numero :  ')
#valor = int(valor)
valor = 0
while valor != secreto:
    valor = int(input('Introcuce un numero :  '))
    if valor > secreto:
        print('Muy alto')
        continue
    if valor < secreto:
        print('muy bajo')
        continue
print ('Acertaste')

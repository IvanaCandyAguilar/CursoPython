def main():
    # bolivia, España, argentina, bolivia, Bolivia,    españa
    paises = input('Lista los paises que conoscas, separados por comas')
    lista_paises = []
    lista_paises = paises.split(',')
    lista_paises = map(lambda x: (str(x).strip()).title(),lista_paises)
    lista_paises = set(lista_paises)
    lista_ordenada = sorted(lista_paises)
    print(lista_paises)

    print('Lista paises ordenada -->',lista_ordenada)
if __name__ == '__main__':
    main()

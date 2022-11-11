from pathlib import Path

def main():
    archivo = 'datos.txt'
    texto = 'esta es una prueba2'
    if existe_archivo(archivo) == False:
        datos = open(archivo,'x')
        datos.close()
    else:
        escribir_texto(texto,archivo)

def existe_archivo(nombre_archivo):
    fichero = Path(nombre_archivo)
    if fichero.is_file() == True:
        return True
    else:
        return False

def escribir_texto(texto,archivo):
    datos = open(archivo,'a')
    datos.write(texto+'\n')
    datos.close()

if __name__ == '__main__':
    main()

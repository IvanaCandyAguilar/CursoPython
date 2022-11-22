import sqlite3
import getpass

def insertar_alumno(nombre,apellido):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()
    query = f"INSERT INTO alumnos(nombre,apellido) VALUES ('{nombre}','{apellido}')"
    #print(query)
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def buscar_alumno(nombre):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM alumnos WHERE nombre='{nombre}'"
    #print(query)

    row = cursor.execute(query)
    data = row.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return data

def main():
    nombre = input('Nombre alumno a buscar: ')
    alumno = buscar_alumno(nombre)
    print(f'ID: {alumno[0]}')
    print(f'NOMBRE: {alumno[1]}')
    print(f'APELLIDO: {alumno[2]}')

def main2():
    nombre = input('Nombre alumno: ')
    apellido = input('Apellido alumno: ')
    insertar_alumno(nombre,apellido)

if __name__=='__main__':
    main()

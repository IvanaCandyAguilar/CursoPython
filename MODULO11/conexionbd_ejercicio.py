import sqlite3
import getpass

def main():
    username = input('Nombre de usuario')
    password = getpass.getpass('Contraseña')
    insertar_usuario(16,username,password)

def main2():
    username = input('Nombre de usuario')
    password = getpass.getpass('Contraseña')
    if verifica_credenciales(username,password):
        print('Login correcto')
    else:
        print('Login incorrecto')

def verifica_credenciales(username, password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()
    query = f"SELECT id FROM users WHERE username='{username}' AND password='{password}'"
    #print('Query a ejecutar',query)
    rows = cursor.execute(query)
    data = rows.fetchone()
    #print('data es ',type(data))
    cursor.close()
    conn.close()

    if data == None:
        return False
    else:
        return True

def insertar_usuario(identificador,usuario, clave):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users VALUES ({identificador},'{usuario}','{clave}')"
    print(query)
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()

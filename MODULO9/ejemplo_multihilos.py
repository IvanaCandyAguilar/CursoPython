import  _thread
import  time

def horaActual(nombre_hilo,tiempo_espera):
    count = 0

    while count <5:
        time.sleep(tiempo_espera)
        count +=1
        print(f'hilo:{nombre_hilo}-{time.ctime(time.time())}')

_thread.start_new_thread(horaActual,('hilo_1',1))
_thread.start_new_thread(horaActual,('hilo_2',2))

print('he dispara ya los hilos')

while True:
    pass

import datetime

def main():
    hora_actual = datetime.datetime.now()
    print("Hora actual",hora_actual.strftime("%X"))

    hora = hora_actual.strftime("%H")
    minuto = hora_actual.strftime("%M")

    if hora_actual.hour > 19:
        print("Es hora de salir")
    else:
        hora_restante = 18 - hora_actual.hour
        minuto_restante = 60 - hora_actual.minute
        print("Tienes trabajo, faltan", hora_restante,"horas:",minuto_restante,"minutos")

if __name__=='__main__':
    main()

import pickle

class Vehiculo:
    marca =''
    modelo = ''

    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def get_marca(self):
        return self.marca

vehiculo1 = Vehiculo('Mercedez','2021')
f = open('datos.bin','wb')
pickle.dump(vehiculo1,f)
f.close()


f = open('datos.bin','rb')
vehiculo2 = pickle.load(f)
print(type(vehiculo2))
print(vehiculo2.get_marca(), 'modelo:',vehiculo2.modelo)

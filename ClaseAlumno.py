class Alumno:
    def __init__(self,nombre,apellido,materia, nota):
        self.nombre = nombre
        self.apellido = apellido
        self.materia = materia
        self.nota = nota
    def mostrar_resultado(self):
        if self.nota > 51:
            print("Aprobado")
        else:
            print("Reprobado")

##----------MAIN-----------------##
alumno1 = Alumno("Ivana","Candy","Programacion I",60)

print("Alumno -->",alumno1.nombre,"Apellido",alumno1.apellido)
print("Nota-->",alumno1.nota)
alumno1.mostrar_resultado()

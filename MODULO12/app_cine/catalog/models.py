from django.db import models

class Pelicula (models.Model):
    nombre = models.CharField(max_length=30)
    director = models.ForeignKey('Director', on_delete=models.CASCADE)
    idioma_original = models.CharField(max_length=30)
    fecha_lanzamiento = models.DateField()
    descripcion = models.TextField()
    imagen = models.ImageField()
    duracion = models.IntegerField()
    genero = (
        ('d', 'drama'),
        ('t', 'terror'),
        ('r', 'romantica'),
        ('f', 'ficcion')
    )
    tipo_pelicula = models.CharField(max_length=1, choices=genero, blank=True)

    def __str__(self):
        return self.nombre

class Director(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    fecha_defuncion = models.DateField(null= True, blank = True)
    biografia = models.TextField()
    imagen = models.URLField()

    def __str__(self):
        return self.nombre + " " + self.apellidos

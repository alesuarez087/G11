from random import randint
from datetime import date
Sexo={'M', 'H'}
class Persona:
    nombre = 'sin nombre'
    edad = 0
    sexo = Sexo
    peso = 0
    altura = 0
    dni=0

    def __init__(self):
        self.dni=randint(10000000,99999999)

    def es_mayor_edad(self):
        if self.edad > 17:
            return True
        else:
            return False

    def print_data(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Sexo:", self.sexo)
        print("Peso:", self.peso)
        print("Altura:", self.altura)
        print("DNI:", self.dni)

class Estudiante(Persona):
    nombre_carrera = 'asignar carrera'
    anio_ingreso = 0
    materias_carrera = 0
    materias_aprobadas = 0

    def avance(self):
        return round(self.materias_aprobadas*100/self.materias_carrera)
    def edad_ingreso(self):
        return self.edad - (date.today().year - self.anio_ingreso)

def diccio(estudiantes):
    diccionario = {}
    for estudiante in estudiantes:
        i = 0
        if estudiante.nombre_carrera not in diccionario.keys():
            for e in estudiantes:
                if e.nombre_carrera == estudiante.nombre_carrera:
                    i+=1
            diccionario[estudiante.nombre_carrera] = i
    print(diccionario.keys())
    print(diccionario.values())

def carga_estudiantes():
    estudiantes = []
    x=Estudiante()
    x.nombre='Ale'
    x.sexo = 'a'
    x.altura = 175
    x.peso=71.5
    x.edad=26
    x.nombre_carrera = 'ISI'
    x.anio_ingreso=2011
    x.materias_carrera=25
    x.materias_aprobadas=18
    estudiantes.insert(0, x);
    x=Estudiante()
    x.nombre='Ale'
    x.sexo = 'a'
    x.altura = 175
    x.peso=71.5
    x.edad=26
    x.nombre_carrera = 'IQ'
    x.anio_ingreso=2011
    x.materias_carrera=25
    x.materias_aprobadas=18
    estudiantes.insert(1, x)
    x=Estudiante()
    x.nombre='Ale'
    x.sexo = 'a'
    x.altura = 175
    x.peso=71.5
    x.edad=26
    x.nombre_carrera = 'IQ'
    x.anio_ingreso=2011
    x.materias_carrera=25
    x.materias_aprobadas=18
    estudiantes.insert(2, x)
    x=Estudiante()
    x.nombre='Ale'
    x.sexo = 'a'
    x.altura = 175
    x.peso=71.5
    x.edad=26
    x.nombre_carrera = 'ISI'
    x.anio_ingreso=2011
    x.materias_carrera=25
    x.materias_aprobadas=18
    estudiantes.insert(3, x)

    return estudiantes


diccio(carga_estudiantes())

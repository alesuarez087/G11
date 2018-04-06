from random import randint

class Persona:
    nombre = 'sin nombre'
    edad = 0
    sexo = 'N'
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

x=Persona()
x.nombre='Ale'
x.sexo = 'M'
x.altura = 175
x.peso=71.5
x.edad=26

x.print_data();
if x.es_mayor_edad():
    print("Es Mayor de Edad")
else:
    print("Es Menor de Edad")

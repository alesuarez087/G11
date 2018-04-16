from  datetime import date, datetime
date_form = '%d/%m/%Y'

class Persona:
    nombre = 'sin nombre'
    nacimiento = datetime.strptime("01/01/1900", date_form)

    def __init__(self, nacimiento):
        self.nacimiento = datetime.strptime(nacimiento, date_form)

    def edad(self):
        i = datetime.today().year - self.nacimiento.year
        if datetime.today() >= self.nacimiento:
            i= i-1
        print(datetime.today()-self.nacimiento)
        return i

    def print_data(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad())


def carga_personas():
    personas = []
    x = Persona("19/08/1991")
    x.nombre = 'Ale'
    personas.insert(0, x)
    x = Persona("28/05/1993")
    x.nombre = 'Fer'
    personas.insert(1, x)
    x = Persona("15/03/1996")
    x.nombre = 'Pablo'
    personas.insert(2, x)
    return personas

def imprimir(personas):
    for i in personas:
        i.print_data();

imprimir(carga_personas())

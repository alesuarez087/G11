from pack.entidades.Socio import Base, Socio
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DatosSocio(object):

    def __init__(self):
        engine = create_engine('sqlite:///so.db')
        Base.metadata.bind = engine
        Base.metadata.create_all(engine)
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        try:
            socio = self.session.query(Socio).filter(Socio.id_socio == id_socio).first()
            return socio

        except Exception as e:
            return None



    def todos(self):
        """
        Devuelve listado de todos los socios en la base de datos.
        :rtype: list
        """
        socios = self.session.query(Socio).all()
        return socios

    def borrar_todos(self):
        """
        Borra todos los socios de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        try:
            socios = self.session.query(Socio).all()
            for s in socios:
                self.session.delete(s)
                self.session.commit()
            return True

        except Exception as e:
            self.session.rollback()
            return False


    def alta(self, socio):
        """
        Devuelve el Socio luego de darlo de alta.
        :type socio: Socio
        :rtype: Socio
        """
        try:
            self.session.add(socio)
            self.session.commit()
            return socio

        except Exception as e:
            print("No se pudo dar de alta el registro: "+str(e))
            self.session.rollback()
            return False


    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        try:
            sq = self.session.query(Socio).filter(Socio.id_socio == id_socio).first()
            self.session.delete(sq)
            self.session.commit()
            return True

        except Exception as e:
            self.session.rollback()
            return False

    def modificacion(self, socio):
        """
        Guarda un socio con sus datos modificados.
        Devuelve el Socio modificado.
        :type socio: Socio
        :rtype: Socio
        """
        try:
            self.session.add(socio)
            self.session.commit()
            return socio

        except Exception as e:
            print("No se pudo dar de alta el registro: "+str(e))
            self.session.rollback()
            return False

    def buscarDni(self, dni):
        try:
            socio = self.session.query(Socio).filter(Socio.dni == dni).first()
            return socio
        except Exception as e:
            return none




def pruebas():
    # alta
    datos = DatosSocio()


    pers = Socio()
    pers.dni = 123
    pers.nombre = "Juan"
    pers.apellido = "Perez"


    socio = datos.alta(pers)
    assert socio.id_socio > 0

    # baja
    assert datos.baja(socio.id_socio) == True

    # buscar
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.id_socio) == socio_2

    # modificacion
    socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
    socio_3.nombre = 'Moria'
    socio_3.apellido = 'Casan'
    socio_3.dni = 13264587
    datos.modificacion(socio_3)
    socio_3_modificado = datos.buscar(socio_3.id_socio)
    assert socio_3_modificado.id_socio == socio_3.id_socio
    assert socio_3_modificado.nombre == 'Moria'
    assert socio_3_modificado.apellido == 'Casan'
    assert socio_3_modificado.dni == 13264587

    # todos
    assert len(datos.todos()) == 2

    # borrar todos
    datos.borrar_todos()
    assert len(datos.todos()) == 0


if __name__ == '__main__':
    pruebas()


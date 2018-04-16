from datetime import datetime, timedelta

date_format = '%d/%m/%Y'


class EJERCICIO:

    def INICIO(self, fecha_ingresada):  # DEVUELVE EL 1/7 ANTERIOR
        fecha = datetime(fecha_ingresada.year, 7, 1)
        if fecha > fecha_ingresada:
            fecha -= timedelta(days=365)
            if fecha_ingresada.year%4==0:
                fecha -= timedelta(days=1)

        print("El 1/7 anterior es: %s/%s/%s" %(fecha.day, fecha.month, fecha.year))

    def FIN(self, fecha_ingresada):
        fecha = datetime(fecha_ingresada.year, 6, 30)
        if fecha > fecha_ingresada:  # DEVUELVE EL 30/6 SIGUIENTE
            fecha += timedelta(days=365)
            if fecha_ingresada.year%4==0:
                fecha += timedelta(days=1)
        print("El 1/7 anterior es: %s/%s/%s" %(fecha.day, fecha.month, fecha.year))

    def SEMANA(self, fecha_ingresada):
        fecha = datetime(fecha_ingresada.year, 7, 1)
        if fecha > fecha_ingresada:
            fecha -= timedelta(days=365)
            if fecha_ingresada.year%4==0:
                fecha -= timedelta(days=1)
        print("Cantidad de semanas:", (fecha_ingresada-fecha).days// 7)


x = EJERCICIO()
fecha = "19/06/1991"
x.INICIO(datetime.strptime(fecha, date_format))
x.FIN(datetime.strptime(fecha, date_format))
x.SEMANA(datetime.strptime(fecha, date_format))

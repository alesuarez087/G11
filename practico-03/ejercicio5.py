import sys
import mysql.connector
import time
from datetime import datetime, date, time, timedelta
import calendar


con=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="dbPersona")

cursor=con.cursor()

idpers = 9
Nom = "Santiago bruno Marelli"
FechaNac = "06/09/2007"
date = datetime.strptime(FechaNac, "%d/%m/%Y")
FechaNac = date.date()
dni = 47395865
altura = 1.59


cursor.execute("UPDATE persona SET IdPersona = %s, Nombre=%s, FechaNacimiento = %s, Altura=%s WHERE DNI=%s", 
	(idpers,Nom,FechaNac,altura,dni))



con.commit()#guarda los cambios



#cerramos las dos conexiones
cursor.close()
con.close()


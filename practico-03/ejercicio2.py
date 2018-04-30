import sys
import mysql.connector
import time
from datetime import datetime, date, time, timedelta
import calendar


con=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="dbPersona")

cursor=con.cursor()

idpers = 12
Nom = "Santiago"
FechaNac = "06/09/2007"
date = datetime.strptime(FechaNac, "%d/%m/%Y")
FechaNac = date.date()
dni = 47395865
altura = 1.55

caux = "INSERT INTO Persona (IdPersona,Nombre, FechaNacimiento,DNI,Altura) VALUES (%s,%s,%s,%s,%s)"
tdatos = (idpers, Nom, FechaNac, dni,altura)
cursor.execute(caux, tdatos)


con.commit()

sql = "SELECT * FROM `Persona` WHERE `DNI`='%s' " %(dni)
cursor.execute(sql)

rows = cursor.fetchone()#me trae el elemento que coincida
print (rows)

cursor.close()
con.close()

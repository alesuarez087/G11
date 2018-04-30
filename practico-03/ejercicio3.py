import sys
import mysql.connector
import time


con=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="dbPersona")

cursor=con.cursor()

idPers = 12
sql = "DELETE FROM `Persona` WHERE `idPersona`='%s'" %(idPers)
cursor.execute(sql)

con.commit()#es para que realice el cambio

#cerramos las dos conexiones
cursor.close()
con.close()

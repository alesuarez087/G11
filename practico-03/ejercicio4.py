import sys
import mysql.connector
import time


con=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="dbPersona")

cursor=con.cursor()

dni = 27590766
sql = "SELECT * FROM `Persona` WHERE `DNI`='%s' " %(dni)
cursor.execute(sql)

rows = cursor.fetchall()#me trae el elemento que coincida

for row in rows:  #rows es todo lo que me regresa el cursor, si tienen 100000 elem me trae todo
    print " IdPersona: %s"  %(row[0]) 
    print " Nombre : %s" %(row[1]) 
    print " Fecha de Nacimineto : %s" %(row[2])
    print " DNI : %s" %(row[3])
    print " Altura : %s" %(row[4]) 


#cerramos las dos conexiones(
cursor.close()
con.close()



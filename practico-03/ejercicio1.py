import sys
import mysql.connector
import time


con=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="dbPersona")

cursor=con.cursor()

sql="CREATE TABLE Persona(IdPersona INT NOT NULL PRIMARY KEY, Nombre CHAR(30), FechaNacimiento Date, DNI INT(13), Altura FLOAT(3,2) );"

cursor.execute(sql)

  
con.commit() #guarda lo que estamos ejecutando
cursor.close() 
con.close()


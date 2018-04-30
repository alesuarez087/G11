
import sys
import mysql.connector
import time
import json


con=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="dbPersona")

cursor=con.cursor()

cursor.execute("SELECT * FROM `Persona`")
#ALTER TABLE people ADD COLUMN (tags json);

   
rows = cursor.fetchall()
rows=str(rows)

datos = json.dumps(rows)
print(datos)


con.close()
cursor.close()

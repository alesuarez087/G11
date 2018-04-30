
import sys
import mysql.connector
import time
import json


con=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="dbPersona")

cursor=con.cursor()

caux="SELECT persona.*, personapeso2.* FROM persona INNER JOIN personapeso2 ON persona.IdPersona = personapeso2.IdPersona "
cursor.execute(caux)

   
rows = cursor.fetchall()

rows=str(rows)

datos = json.dumps(rows)
print(datos)


con.close()
cursor.close()

import sys
import mysql.connector
import time
from datetime import datetime, date, time, timedelta
import calendar

try:
    con=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="dbPersona")
    cursor=con.cursor()
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database  no existe!!")
  else:
    print(err)

def buscarPersona():
    while True:
        try:
            dni = int(raw_input("Escriba el nro de DNI de la persona: "))
            sql = "SELECT idPersona FROM `Persona` WHERE DNI = '%s' " %(dni)
            cursor.execute(sql)
            rows = cursor.fetchall()#me trae el elemento que coincida
            if rows==[] :
                print("la persona no existe!!!")
                continue
            else:
                for row in rows:
                    idpers = (row[0])
                IngresarPesoPersona(idpers,dni)
            break
        except ValueError :
            print ("El DNI debe ser un nro!!!")


             

            
def IngresarPesoPersona(idpers,dni):
    peso= int(raw_input( "Ingresar el Peso Para la Persona con DNI " + str(dni) + " : " ))
    fecha = str(raw_input("Ingresar fecha de peso con formato D/M/A: "))
    date_object = datetime.strptime(fecha, "%d/%m/%Y")
    fecha1 = date_object.date()
    caux = "SELECT Fecha FROM PersonaPeso2 WHERE (Fecha > '%s') AND (idPersona = '%s') " %(fecha1,idpers)
    cursor.execute(caux)
    rows = cursor.fetchall()#me trae el elemento que coincida
    if cursor.rowcount==0 :
         caux = 'INSERT INTO PersonaPeso2 (IdPersona, Fecha, Peso) VALUES (%s,%s,%s)'
         tdatos = (idpers, fecha1, peso)
         cursor.execute(caux, tdatos)
         con.commit()
         print ( "El peso para la fecha: "+ str(fecha) + "fue registrada con exito")
    else :
        print ("ya existe un registro con fecha posterior a : " + str(fecha))
       
    
      

buscarPersona()


#cerramos las dos conexiones
cursor.close()
con.close()

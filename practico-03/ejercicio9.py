"""Hacer un programa Python para acceder a la tabla Personas y PersonaPeso y buscar el registro de una persona identificada
por su DNI, mostrar los datos de la persona y de su historial de peso.

"""
import sys
import mysql.connector
import time
from datetime import datetime, date, time, timedelta
import calendar
import os


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
                idpers = "%s" %(rows[0])
                mostrardatosPers(idpers,dni)
            break
        except ValueError :
            print ("El DNI debe ser un nro!!!")

def mostrardatosPers(idpers,dni):
    caux="SELECT persona.*, personapeso2.* FROM persona INNER JOIN personapeso2 ON persona.IdPersona = personapeso2.IdPersona WHERE persona.IdPersona = '%s' " %(idpers)
    cursor.execute(caux)
    rows = cursor.fetchone() #me trae la persona sellecionada
    print"idPersona: %s - Nombre : %s - Fecha NAcimiento: %s - DNI: %s - Altura : %s " %(rows[0] , rows[1] , rows[2],rows[3], rows[4])
    rows = cursor.fetchall() # me trae todos los registros peso
    for row in rows:
        print "Fecha: %s - Peso: %s" %(row[7] , row[8])
        

buscarPersona()


#cerramos las dos conexiones
cursor.close()
con.close()
          

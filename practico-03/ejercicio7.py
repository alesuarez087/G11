
import sys
import mysql.connector
import time


con=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="dbPersona")

cursor=con.cursor()


cursor.execute("ALTER TABLE `Persona` CONSTRAINT IdPersona  INT(15) NOT NULL PRIMARY KEY ;") #Primero modifico el IdPersona de Persona como NOT NULL


cursor.execute("CREATE TABLE PersonaPeso2(idPeso INT NOT NULL AUTO_INCREMENT, IdPersona INT NOT NULL , Fecha Date, Peso INT, PRIMARY KEY(idPeso),INDEX (IdPersona), FOREIGN KEY (IdPersona) REFERENCES Persona(IdPersona) )ENGINE=InnoDB;")



con.commit()#es para que realice el cambio

#cerramos las dos conexiones
cursor.close()
con.close()

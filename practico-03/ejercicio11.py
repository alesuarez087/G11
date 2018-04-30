import decimal


def dividir():
    while True:
        try:
            X = float(input("Ingrese el numero X : "))
            Y = float(input("Ingrese el numero Y : "))
            Z = (X/Y)
            return Z
            break
        except ZeroDivisionError:
            print("El divisor no puede ser cero")
        except :
            print ("debe ingresar un numero")
            




print (round (dividir(),5))



 

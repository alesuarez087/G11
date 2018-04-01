def esPrimo(nro):
   if nro < 3:
       return True
   else:
       for i in range(2, nro):
           if nro%i == 0:
               return False
       return True

nro = int(input("Ingrese un nro: "))
if esPrimo(nro):
   print("Es primo")
else: print("No es primo")

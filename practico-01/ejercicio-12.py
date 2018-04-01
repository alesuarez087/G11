def sum(nro):
   n = 0
   for i in range(1, (nro+1)):
       n = n + i
   return n

nro = int(input("Ingrese un nro: "))
print("La suma de todos los numeros hasta el que ingreso es: ", sum(nro))
